<html>
    <head>
                <title><?php echo getcwd(); ?></title>
                <style type='text/css'>
                        body {
                            font-family: "Candara", sans-serif;
                            font-size: 9pt;
                            line-height: 10.5pt;
                        }
                        div.pic h3 { 
                            font-size: 11pt;
                            margin: 0.5em 1em 0.2em 1em;
                        }
                        div.pic p {
                            font-size: 11pt;
                            margin: 0.2em 1em 0.1em 1em;
                        }
                        div.pic {
                            display: block;
                            float: left;
                            background-color: white;
                            border: 1px solid #ccc;
                            padding: 2px;
                            text-align: center;
                            margin: 2px 10px 10px 2px;
                            -moz-box-shadow: 7px 5px 5px rgb(80,80,80);    /* Firefox 3.5 */
                            -webkit-box-shadow: 7px 5px 5px rgb(80,80,80); /* Chrome, Safari */
                            box-shadow: 7px 5px 5px rgb(80,80,80);         /* New browsers */  
                        }
                        a { text-decoration: none; color: rgb(80,0,0); }
                        a:hover { text-decoration: underline; color: rgb(255,80,80); }
                        figure {
                                display: table;
                                width: 1px; /* This can be any width, so long as it's narrower than any image */
                                }
                        img, figcaption {
                                display: table-row;
                                }
                </style>

    </head>


    <body>
            <h4>&copy G. Petrucciani (CERN), R. Plestina (IHEP-CAS)</h4>

            <?PHP
                if (file_exists("title.txt")){
                    $page_title = file_get_contents("title.txt");
                    print "<h1>$page_title</h1>";
                }
                print "<h3>".getcwd()."</h3>";
                if (file_exists("basic.info")){
                    print "<h2><a name='basic_info'>Basic information</a></h2>";
                    $file_handle = fopen("basic.info", "rb");

                    while (!feof($file_handle) ) {
                            $line_of_text = fgets($file_handle);
                            $parts = explode('=', $line_of_text);
                            print $parts[0] . $parts[1]. "<BR>";
                    }
                    fclose($file_handle);
                }
            ?>
            

            
            <h2><a name="plots">Plots</a></h2>
            <p>
                <form>Filter: 
                    <input type="text" name="match" size="30" value="<?php if (isset($_GET['match'])) print htmlspecialchars($_GET['match']);  ?>" /><input type="Submit" value="Search" />
                </form>
            </p>

            <div>
                    <?PHP
                    // ____________________________________________________________________________________________________________
                    $displayed = array();
                    if ($_GET['noplots']) {
                        print "Plots will not be displayed.\n";
                    } else {
                        $other_exts = array('.pdf', '.cxx', '.eps', '.root', '.txt','.C','.gif');
                        $filenames = glob("*.png"); sort($filenames);
                        foreach ($filenames as $filename) {
                            if (isset($_GET['match']) && !fnmatch('*'.$_GET['match'].'*', $filename)) continue;
                            array_push($displayed, $filename);
                            print "<div class='pic'>\n";
                            print "<h3><a href=\"$filename\">$filename</a></h3>";
//                             print "<a href=\"$filename\"><img src=\"$filename\" style=\"border: none; width: 300px; \"></a>";
                            $others = array();
                            $caption_text = '';
                            foreach ($other_exts as $ex) {
                                $other_filename = str_replace('.png', $ex, $filename);
                                if (file_exists($other_filename)) {
//                                     array_push($others, "<a class=\"file\" href=\"$other_filename\">[" . $ex . "]</a>");
                                    if ($ex != '.txt') {
                                        array_push($others, "<a class=\"file\" href=\"$other_filename\">[" . $ex . "]</a>");
                                        array_push($displayed, $other_filename);
                                        
                                    }
                                    
                                    else {
                                        $caption_text = file_get_contents($other_filename);
                                    }
                                }
                            }
//                             print "<a href=\"$filename\"><figure><img src=\"$filename\" style=\"border: none; width: 300px; \"><figcaption>$caption_text</figcaption></figure></a>";
                            print "<figure><a href=\"$filename\"><img src=\"$filename\" style=\"border: none; width: 300px; \"></a><figcaption>$caption_text</figcaption></figure>";
                            if ($others) print "<p>View as ".implode(', ',$others)."</p>";
                           
                            
                            print "</div>";
                        }
                    }
                    // ____________________________________________________________________________________________________________
                    ?>

            </div>
            <div style="display: block; clear:both;">
                    <h2><a name="files">Other</a></h2>
                    <ul>
                    <?PHP
                    // ____________________________________________________________________________________________________________
                    foreach (glob("*") as $filename) {
                        if ($_GET['noplots'] || !in_array($filename, $displayed)) {
                            if (isset($_GET['match']) && !fnmatch('*'.$_GET['match'].'*', $filename)) continue;
                            if ($filename=='index.php') continue;
                            if (is_dir($filename)) {
                                print "<b><li><a href=\"$filename\">$filename</a></li></b>";

                            } else {
                                print "<li><a href=\"$filename\">$filename</a></li>";
                            }
                        }
                    }
                    // ____________________________________________________________________________________________________________
                    ?>
                    </ul>
            </div>
            
            
            
            
                        <!-- begin htmlcommentbox.com -->
<!--             <div id="div_comments" style="border: none; width: 500px;" > -->
                                <!-- begin htmlcommentbox.com -->
                <div id="HCB_comment_box"><a href="http://www.htmlcommentbox.com">Comment Box</a> is loading comments...</div>
                <link rel="stylesheet" type="text/css" href="//www.htmlcommentbox.com/static/skins/shady/skin.css" />
                <script type="text/javascript" id="hcb"> /*<!--*/ if(!window.hcb_user){hcb_user={};} (function(){var s=document.createElement("script"), l=(hcb_user.PAGE || ""+window.location), h="//www.htmlcommentbox.com";s.setAttribute("type","text/javascript");s.setAttribute("src", h+"/jread?page="+encodeURIComponent(l).replace("+","%2B")+"&mod=%241%24wq1rdBcg%24wIIsmS1kJxbC4%2Ffed9E7M1"+"&opts=16662&num=10");if (typeof s!="undefined") document.getElementsByTagName("head")[0].appendChild(s);})(); hcb_user.submit="";/*-->*/ </script>
                <!-- end htmlcommentbox.com -->
                
<!--             </div> -->
            <!-- end htmlcommentbox.com -->
    </body>
</html>

