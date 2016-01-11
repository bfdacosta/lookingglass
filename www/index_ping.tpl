<!DOCTYPE html>
<HTML>
<HEAD>
<META HTTP-EQUIV="Content-Type" CONTENT="text/html; charset=UTF-8">
<LINK REL="stylesheet" TYPE="text/css" HREF="site.css">
<link rel="icon" type="image/png" href="/favicon.png">
</HEAD>
<BODY>

<DIV CLASS="header" ID="header">
<H1>Internet Message Control Protocol - ICMP</H1>
</DIV>

<DIV CLASS="body" ID="body">
<form action="/ping" class="form-horizontal" method="GET">
<fieldset>
<legend>Ping Tool</legend>
<p></p>
<div class="control-group">
  <b><label class="control-label" for="address">IP Address: </label></b>
  <div class="controls">
    <input id="address" name="address" type="text" placeholder="1.1.1.1" class="input-large" required="">
    <p class="help-block">Help: Insert IP address</p>
  </div>
</div>
<button id="save" name="save" value="save" class="btn btn-primary">Go Baby Go</button>
</fieldset>
</form>
</DIV>
</BODY>
</HTML>
