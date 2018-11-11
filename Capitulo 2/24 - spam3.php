<?php
if( $_SERVER["REQUEST_METHOD"] == "POST" ){
    $FROM = $_POST["FROM"];
    $TO = $_POST["TO"];
    $SUBJECT = $_POST["SUBJECT"];
    $BODY = $_POST["BODY"];
    mail($TO, $SUBJECT, $BODY, "From:" . $FROM);
}
?>