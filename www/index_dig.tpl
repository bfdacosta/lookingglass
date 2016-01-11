<!DOCTYPE html>
<HTML>
<HEAD>
<META HTTP-EQUIV="Content-Type" CONTENT="text/html; charset=UTF-8">
<LINK REL="stylesheet" TYPE="text/css" HREF="site.css">
<link rel="icon" type="image/png" href="/favicon.png">
</HEAD>
<BODY>

<DIV CLASS="header" ID="header">
<H1>Domain Name Service - DNS</H1>
<H2>Query Tool</H2>
</DIV>

<DIV CLASS="body" ID="body">
<form action="/dig" class="form-horizontal" method="GET">
<fieldset>
<legend>Domain Query</legend>
<p></p>
<div class="control-group">
  <b><label class="control-label" for="domain">Domain: </label></b>
  <div class="controls">
    <input id="domain" name="domain" type="text" placeholder="google.com" class="input-large" required="">
    <p class="help-block">Help: Insert the domain name</p>
  </div>
<div class="controls">
    <input id="dns" name="dns" type="text" placeholder="8.8.8.8" class="input-large" required="">
    <p class="help-block">Help: Insert the DNS Server to query</p>
  </div>
<div class="controls">
    <input id="query_type" name="query_type" type="text" placeholder="A" class="input-large" required="">
    <p class="help-block">Help: Insert query type eg. A/SOA/PTR/..</p>
  </div>
</div>
<button id="save" name="save" value="save" class="btn btn-primary">Go Baby Go</button>
</fieldset>
</form>
</DIV>
</BODY>
</HTML>
