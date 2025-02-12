<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $number = escapeshellarg($_POST['number']);  // Secure input
    $text = escapeshellarg($_POST['text']);  // Secure input

    // Execute the Python script and capture output
    $command = "python3 process.py $number $text";
    $output = shell_exec($command);

    echo "<h2>Results:</h2>";
    echo $output;
} else {
    echo "<p>Error: Invalid request</p>";
}
?>
