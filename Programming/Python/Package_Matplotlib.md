# Matplotlib

A **Mat**hematical **plot**ting **lib**rary for Python.

```python
import matplotlib.pyplot as plt
```

When using Jupyter Notebooks, also add:
%matplotlib inline

Make a plot, quick and dirty:
t = np.arange(0., 5., 0.2)
# red dashes, blue squares and green triangles
plt.plot(t, t^2)
Can combine multiple plots in a single plot() call:
plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')
plt.plot(t, t^2, drawstyle='steps-pre')
plt.show()

Use more control:
f = plt.figure()				# Make a figure (canvas).
- Default fig size is (6.4, 4.8) (inches?)
f = plt.figure(figsize=(12,3))	# Control size of figure.
ax = fig.add_axes([0,0,1,1])	# Add x,y axes object to figure.

ax1 = f.add_subplot(121)		
ax2 = f.add_subplot(122)

Or even:
f, ax = plt.subplots()	# Make fig and ax at same time.
f, ax = plt.subplots(nrows=2, ncols=3, sharex=True)	# Make 6 axes that share same labels.
f,(ax1,ax2) = plt.subplots(1,2)		# Make different axes objects for more control.

plt.axis( <xvals>.min() , <xvals>.max() , <yvals>.min() , <yvals>.max() )	# control axis range

Axes:
ax.set_ylim([<ymin>,<ymax>])		# sets y bounds from <ymin> to <ymax>    # plt equivalent: plt.ylim( (ymin, ymax) )
ax.tick_params(axis='y', labelsize=8)	# adjust size of numbers on y-axis
plt.xscale('log')					# make x-axis log scale
ax.set_xscale('log')
ax.set_title('My Plot')    # plt equivalent: plt.title('Yo!')
ax.set_xlabel(r'$<\LaTeX!!!>$')		# Use LaTeX commands 
xlabel="$lep$: $p_{T}$ / GeV")		# can separate LaTeX font from regular font
https://matplotlib.org/users/mathtext.html

ax.grid()	# add a grid within plot

If tick labels (like numbers) are overlapping, 
you can reduce the number of labels that appear:
ax.xaxis.set_major_locator(plt.MaxNLocator(3))    # Will only show 3 labels on x-axis.


Remember: You draw plots on axes, so use your ax object to do the plotting!
ax.plot(x, y)
ax.plot(x, np.sin(x), color='red', label='sine fn', alpha=0.6    # alpha is transparency
		linestyle='--', linewidth=2, marker='s',   	# square markers
)	

- To add another graph to the same axes, just do: ax.plot(<graph>)
- Other useful linestyles: -- -. : 'steps'

Add x10^(-3) to your axis labels:
ax.ticklabel_format(axis="x", style="sci", scilimits=(3,3), useMathText=True)

Legend:
ax.legend(loc='upper left')

Text box:ax.text(x, y, "Some words", horizontalalignment='center', verticalalignment='center', transform=ax.transAxes)
- Using `transform=ax.transAxes` puts x,y in terms of axes coordinates (as opposed to data coordinates)
Example:
props = dict(boxstyle='square', facecolor='whitesmoke', edgecolor='blue', alpha=0.8)
ax.text(0.9915, 0.986, textstr, transform=ax.transAxes, fontsize=textsize_legend, verticalalignment='top', horizontalalignment='right',bbox=props)


Make a colorbar and put limits on it:
plt.colorbar(im, ax=ax, boundaries=np.linspace(0,160000,10000))

Clear a figure, to save RAM:
plt.clf()
- figure will still be drawn to in future plots.
------
You can change your default matplotlib settings:
- This way all your plots will be uniform just the way you like. 
- You can control all the little individual features, like font, linewidth, and axes properties.

See what your current matplotlib default settings are:
import matplotlib as mpl
print(mpl.rcParams)

Change the defaults: 


Do the same thing a different way:
mpl.rcParams['lines.marker'] = 'o'
mpl.rcParams['hist.bins'] = 50
mpl.rcParams['font.family'] = ['serif']
mpl.rcParams['xtick.direction'] = 'in'

Find where your current matplotlibrc file is loaded from:
mpl.matplotlib_fname()
- modify this file to get permanent changes. 
Return to default settings:
mpl.rcdefaults()

Define your own plot styles in a file called CMS_plot.mplstyle:
axes.titlesize : 24
axes.labelsize : 20
lines.linewidth : 3
lines.markersize : 10
xtick.labelsize : 16
ytick.labelsize : 16

plt.style.use('CMS_plot')
- This uses the plot settings stored in 'CMS_plot.mplstyle'.
- Store your .mplstyle files in: mpl_configdir/stylelib/<mystyle>.mplstyle
- Find mpl_configdir/ by doing: mpl.get_configdir()

Reload the library of style sheets:
plt.style.reload_library()

Combine style sheets:
plt.style.use(['CMS_plot', 'dark_theme', 'large_font'])
- Each of the three styles above must have its own .mplstyle file.

See what available styles there are:
print(plt.style.available)

Use a style only temporarily:
with plt.style.context('<mystyle>'):
    plt.plot(data)
plt.show()



If Python complains about not finding font files, do:
import matplotlib.font_manager as font_manager; font_manager._rebuild()