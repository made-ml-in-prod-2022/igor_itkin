TEMPLATE = '''
<?xml version="1.0" ?><!DOCTYPE html  PUBLIC '-//W3C//DTD XHTML 1.0 Strict//EN'  'http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd'>
<html>
<head>
<h1>
DATA REPORT

{date}
</h1>
</head>
<body>
<h2>
Features statistics
</h2>
{statistics}

<h2>
NA values
</h2>
{na_values}

<h2>
Categorical features values
</h2>
{cat_values}
<h2>
Values distribution
</h2>

<img style='display:block; width:1200px;height:600px;' id='base64image'
   src='data:image/jpeg;base64, {encoded_image}' />
</body>

</html>
'''