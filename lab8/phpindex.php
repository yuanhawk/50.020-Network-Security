<?php
  $cspheader = "Content-Security-Policy:".
               "default-src 'self';".
               "script-src 'self' 'nonce-111-111-111' *.example70.com".
               " 'nonce-222-222-222' *.example60.com";
  header($cspheader);
?>

<?php include 'index.html';?>

