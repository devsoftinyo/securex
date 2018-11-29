<?php
require_once("functions.php");
$files = getDirContents('../../bayipanel', '/\.php$/');

foreach($files as $file){
  echo find_linenumber('$sql',$file);
}

?>
