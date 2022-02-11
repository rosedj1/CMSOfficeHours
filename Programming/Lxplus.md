# Lxplus, EOS, and more

Log onto node `N`: `your_username@lxplusN.cern.ch`

Display plots: `display yourplot.png &`

## Root Redirector

Access CMS files located anywhere on any computer:

Here's how to access a HPG file from lxplus:

```bash
cmsenv
voms-proxy-init -voms cms
root://cmsxrootd.fnal.gov//store/user/path_to_file.root
```

CHECK THIS:

```bash
root://eoscms.cern.ch//eos/cms/store/data/Run2017B/MuonEG/MINIAOD/31Mar2018-v1/100000/049A7BE5-7037-E811-9CDE-3417EBE706C6.root
```

## EOS

[EOS quick tutorial for beginners.](https://cern.service-now.com/service-portal?id=kb_article&n=KB0001998)

## CERNBox

Store plots, presentations, and more on the CERN cloud.

Follow [these instructions](https://cernbox-manual.web.cern.ch/cernbox-manual/en/web/personal_website_content.html)
to create a set up a `www` directory in your 

----------

**ELISA'S INSTRUCTIONS:**
Hi Jake, 
I followed instructions here:
https://webservices.web.cern.ch/webservices/
going to "create a new website".

1. Create your website (https://webservices.web.cern.ch/webservices/Services/CreateNewSite/Default.aspx) 
     - Choose "Personal homepage"
    - Eos directory with path /eos/user/e/elfontan/www
2. From CERN box page, share your folder www with a:wwweos (wwweos is the service account), removing the tick "can modify"
3. Create a .htaccess file with the following lines [1] and put it in your www directory
4. To show plots in the page (and not only the list), type something like:
/eos/user/e/elfontan/Run2Legacy/publishDir   /eos/user/e/elfontan/www/Run2Legacy_ValidationPlots/ index.php
Here you can find index.php (move it in www dir) and publishdir (you have to make it executable and put it where you want! I have it before www dir) files:
/eos/user/e/elfontan/ZpX_Checks/index.php
/eos/user/e/elfontan/ZpX_Checks/publishDir

If you need additional instructions, look at this page:
https://cernbox-manual.web.cern.ch/cernbox-manual/en/web/

Let me know if you manage to use this instructions!
Cheers,
Elisa


[1]
Options +Indexes

SSLRequireSSL # The modules only work using HTTPS
AuthType shibboleth
ShibRequireSession On
ShibRequireAll On
ShibExportAssertion Off

Require valid-user
Require ADFS_GROUP "cms-members"

----------

`https://cernbox.cern.ch/`

- Your website: `https://<your_username>.web.cern.ch/`
- Manage the site: `https://webeos.cern.ch`
- How to [store plots on your CERNBox website].

### Resources

- [All the info you need for CERNBox](https://cernbox-manual.web.cern.ch/cernbox-manual/en/).
