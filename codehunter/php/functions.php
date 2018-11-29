<?php
function getDirContents($dir, $filter = '', &$results = array()) {
    $files = scandir($dir);

    foreach($files as $key => $value){
        $path = realpath($dir.DIRECTORY_SEPARATOR.$value);

        if(!is_dir($path)) {
            if(empty($filter) || preg_match($filter, $path)) $results[] = $path;
        } elseif($value != "." && $value != "..") {
            getDirContents($path, $filter, $results);
        }
    }

    return $results;
}

function find_linenumber($string,$file){
    $search      = $string;
    $lines       = file($file);
    $line_number = false;

  while (list($key, $line) = each($lines) and !$line_number) {
    $line_number = (strpos($line, $search) !== FALSE) ? $key + 1 : $line_number;

  }

    $linex_number = $line_number - 1;


  if(!empty($line_number)){
    echo "<textarea>$lines[$linex_number]</textarea>";
    echo "<strong>$file</strong> dosyasının $line_number . satırında bulundu !<br>";
  }
}


?>
