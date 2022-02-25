"""Unbinned Gaussian Fits using RooFit

Goal:
    Investigate the differences between binned and unbinned fits.
Workflow:
    (1) Use numpy to generate 10,000 random points from a
        Gaussian pdf: G(mu=91.1876, sigma=2.4952).
    (2) Histogram these data using bin widths = 0.25.
    (3) Write a function which takes in your hist
        and fits the histogram with a Gaussian curve. 
        Return the fit parameters (mu_fit, mu_sigma).
    (4) Write a different function which takes in the
        original, unbinned data and fits it with a Gauss pdf.
        Return the fit parameters (mu_fit_unbin, mu_sigma_unbin).
        This uses the method of maximum likelihood.
    (5) Make a plot of the unbinned fit on top of the binned 
        distribution. Make the fit curve red.
Considerations:
    (1) How do the binned and unbinned fit parameters compare?
    (2) How do the fit parameters compare to the true average and 
        standard deviation of the unbinned data?
    (3) Plot the (diff_mu = mu_fit_unbin - mu_fit) as a function
        of (number of points generated).
        Maybe use increments of 10 points. 
    (4) Is there some point at which the binned fit does just as 
        well as the unbinned fit?
"""

def RooFit_gaus_fit(data, binned_fit=True, fit_range=None, xframe=None, 
                    count=1, # Possibly deprecated.
                    x_label="Independent Var", 
                    color=4, # Deprecated.
                    draw=False, verbose=False,
                    line_color=4, marker_color=1):
    """
    Perform a binned or unbinned Gaussian fit to some data using RooFit.
    Return a 2-tuple: 
        (best_fit_stats_ls, xframe_with_gauss)
        where: best_fit_stats_ls: [mean, mean_err, sigma, sigma_err].

    Parameters
    ----------
    data : list (or array-like) or ROOT.TH1
        The data to be fit with a Gaussian function.
        NOTE:
        If the data is of type `list` or `numpy.ndarray` then an *unbinned fit* is performed.
        If the data is of type `ROOT.TH1` then a *binned fit* is performed.
    binned_fit : bool, optional
        If True, do a binned fit. `data` must be of the correct type.
        Otherwise do an unbinned fit.
    xframe : ROOT.RooRealVar.frame, optional
        Essentially a canvas onto which the data and Gaussian fit will be drawn.
        If a frame is not provided, a frame will be created.
    fit_range : 2-elem list, optional
        [x_min, x_max]
        Range along x-axis over which to do the fit.
        If none is provided, fit range will be [data.min(), data.max()].
    count : int, optional
        An iterator to help with setting the legend of best-fit params.
        Used to position the fit stats labels on the plot. 
        Also used to color the fit lines. 
        Example: count=1 is kBlack, count=2 is kRed
    x_label : str, optional
        Label of the x-axis. Can accommodate ROOT LaTeX by using '#'.
    color : ROOT.TColor, optional
        Color of the fit line.
    draw : bool
        If True, then draw on the frame.
    verbose : bool
        If True, print juicy debug info.
    
    Returns
    -------
    A 2-tuple: (fit_stats_ls, xframe)
        fit_stats_ls : 4-element list
            The best-fit parameters from the fit: [mean, mean_err, sigma, sigma_err]
        xframe : ROOT.RooFit.RooRealVar.frame
            Essentially a canvas with the data and Gaussian fit drawn on.
            Still need to do xframe.Draw() onto a TCanvas.
    """
    r.RooMsgService.instance().setStreamStatus(1,False)
    # Investigate data.
    if isinstance(data, r.TH1):
        msg = (
            f"[ERROR] Your data are in a histogram, but you are requesting an unbinned fit.\n"
            f"        Perhaps you should set `binned_fit = True`."
            )
        assert binned_fit, msg
        x_min = data.GetBinLowEdge(0)
        x_max = Root_Hist_GetLastBinRightEdge(data)
        x_avg = data.GetMean()
        x_std = data.GetStdDev()
    elif (isinstance(data, list) or isinstance(data, np.ndarray)):
        msg = (
            f"[ERROR] Your data are array-like, but you are requesting a binned fit.\n"
            f"        Perhaps you should set `binned_fit = False`."
            )
        assert not binned_fit, msg
        data = np.array(data)
        x_min = data.min()
        x_max = data.max()
        x_avg = data.mean()
        x_std = data.std()
    else:
        raise TypeError(f"Data (type: {type(data)}) must of type `list`, `numpy.ndarray`, or `ROOT.TH1`.")

    # Make fit variables.
    x_roofit = r.RooRealVar("x_roofit", x_label, x_min, x_max)
    mean = r.RooRealVar("mean","Mean of Gaussian", x_avg, x_min, x_max)
    sigma = r.RooRealVar("sigma","Width of Gaussian", x_std, 0, 999999)
    gauss = r.RooGaussian("gauss","gauss(x_roofit,mean,sigma)", x_roofit, mean, sigma)
    
    # Prepare RooFit data container.
    if isinstance(data, r.TH1):
        # Make RooDataHist.
        ls = r.RooArgList(x_roofit)
        roodata = r.RooDataHist("roodata", "RooDataHist", ls, data)
    else:
        # Make RooDataSet.
        ptr = array('f', [0.])
        tree = r.TTree("tree", "tree")
        tree.Branch("x_roofit", ptr, "x_roofit/F")
        for val in data:
            ptr[0] = val
            tree.Fill()
        roodata = r.RooDataSet("roodata","dataset from tree", tree, r.RooArgSet(x_roofit))

    # Modify fit range, if needed.
    if fit_range is None:
        fit_x_min = x_min
        fit_x_max = x_max
    else:
        fit_x_min = fit_range[0]
        fit_x_max = fit_range[1]
        
    # Find and fill the mean and sigma variables.
    if (verbose):
        result = gauss.fitTo(roodata, r.RooFit.Range(fit_x_min, fit_x_max))
    else:
        result = gauss.fitTo(roodata, r.RooFit.Range(fit_x_min, fit_x_max), r.RooFit.PrintLevel(-1))
    
    # Optional: draw the fit to the frame.
    if (draw):
        if xframe is None:
            # xframe = x.frame(r.RooFit.Title("Some title here?"))
            xframe = x.frame(r.RooFit.Range(fit_x_min, fit_x_max))
        # Draw data and then the fit.
        # data.Draw()
        # Put the fit params on the plot.
        # if (draw_stats):
        # else:
            # Don't need to keep drawing to canvas...
        #     # Probably using an iterative Gaus fit. Draw to previous canvas. 
        #     data.Draw("same")
        roodata.plotOn(xframe, r.RooLinkedList())
        roodata.plotOn(xframe, r.RooFit.MarkerColor(marker_color))
        gauss.plotOn(xframe,   r.RooFit.LineColor(line_color), r.RooFit.Range(fit_x_min, fit_x_max))
        # color = color_dict_RooFit[count]
        # Put the Gaussian fit parameters on the plot.
        # text_y_min = 0.92 - 0.11*(count-1)
        gauss.paramOn(xframe, 
            r.RooFit.Layout(0.13, 0.40, text_y_min)  # (x_min, x_max, y_max) as fraction of canvas width.
            )
        # text_y_min = 0.95 - 0.11*(count-1)  # In the top left corner of TCanvas("c","c",600,600).
        text_y_min = 0.88 - 0.11*(count-1)
        # Set xframe params.
        xframe.getAttText().SetTextSize(0.020)
        xframe.getAttText().SetTextColor(line_color)
        r.gStyle.SetOptStat("iouRMe")
        xframe.Draw("same")
    
#     pavelabel_x_start = ( float(x_max) + float(x_min) ) * 0.65
#     title = r.TPaveLabel( pavelabel_x_start, 300, x_max, 350, 'Come on dude!' )
#     title.SetTextFont( 50 )
#     title.Draw("same")

    # Make a legend.
#     leg_text  = "#splitline{#mu = %.5f #pm %.5f}" % (mean.getVal(),  mean.getError())
#     leg_text += "{#sigma = %.5f #pm %.5f}" % (sigma.getVal(),  sigma.getError())
#     leg = r.TLegend(0.10, 0.75, 0.35, 0.9)
#     leg = r.TLegend(0.03, 0.80, 0.20, 0.9)
#     leg = r.TLegend()
#     leg.AddEntry("hist", leg_text, "pel")
#     leg.Draw("same")
    
#     leg_text  = "#splitline{#mu = %.3f #pm %.3f}" % (mean.getVal(),  mean.getError())
#     leg_text += "{#sigma = %.3f #pm %.3f}" % (sigma.getVal(),  sigma.getError())

    # fixOverlay()
    fit_stats_ls = [mean.getVal(), mean.getError(), sigma.getVal(), sigma.getError()]
    return (fit_stats_ls, xframe)