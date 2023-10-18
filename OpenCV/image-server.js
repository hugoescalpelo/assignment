const express = require('express');
const app = express();
const path = require('path');

// Assuming your images are in the '/home/hugo/Pictures/' directory
const imageDirectory = '/home/hugo/Pictures/';

// Create a dynamic route to serve images based on a parameter
app.get('/images/:imageName', (req, res) => {
  const imageName = req.params.imageName;
  const imagePath = path.join(imageDirectory, imageName);

  // Use the "express.static" middleware to serve the image
  res.sendFile(imagePath, (err) => {
    if (err) {
      // Handle errors (e.g., image not found)
      res.status(404).send('Image not found');
    }
  });
});

// Your other routes and middleware can go here

// Start your Express server
app.listen(3000, () => {
  console.log('Server is running on port 3000');
});
