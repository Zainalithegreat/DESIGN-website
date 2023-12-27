<?php 
session_start();

	include("connection.php");
	include("functions.php");

	$user_data = check_login($con);

?>

<!DOCTYPE html>
<html>
<head>
	<title>My website</title>
</head>
<body>

	<a href="logout.php">Logout</a>
	<h1>This is the index page</h1>
	<a href="image_upload.html">Upload image?</a>
	<?php var_dump(file_exists("image_upload.html")); ?>

	<a href="Paint.html">Want to Paint</a>
	<?php var_dump(file_exists("Paint.html")); ?>


	<br>
	Hello, <?php echo $user_data['user_name']; ?>
</body>
</html>