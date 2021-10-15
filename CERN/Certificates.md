# Certificates

In order to use Data Aggregation Service (DAS),
your browser (e.g., Mozilla Firefox) will need to present
a **valid Grid Certificate** (a file in `.p12` format).

* Follow [these instructions](https://twiki.cern.ch/twiki/bin/viewauth/CMS/DQMGUIGridCertificate)
if you need a Grid Certificate.

In order to do `voms-proxy-init` the Grid Certificate must be
converted to a public-private key pair (`usercert.pem`, `userkey.pem`):

```bash
mkdir $HOME/.globus
openssl pkcs12 -in YOUR_GRID_CERT_NAME.p12 -clcerts -nokeys -out $HOME/.globus/usercert.pem
openssl pkcs12 -in YOUR_GRID_CERT_NAME.p12 -nocerts -out $HOME/.globus/userkey.pem
# NOTE: If you get a "Permission denied" error, then do:
# `chmod 755 usercert.pem userkey.pem`
# then rerun the above commands.
# Finally, give only you read permissions.
chmod 400 $HOME/.globus/userkey.pem $HOME/.globus/usercert.pem
```
