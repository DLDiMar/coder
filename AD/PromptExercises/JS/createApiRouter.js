const express = require('express');

function createApiRouter(inputRoute) {
  const router = express.Router();
  const routeParts = inputRoute.split('/');

  // Define the API routes
  router.get('/', (req, res) => {
    res.json({ message: `Welcome to the ${inputRoute} API!` });
  });

  router.get(`/${routeParts[1]}`, (req, res) => {
    res.json({ message: `You are accessing the ${routeParts[1]} endpoint` });
  });

  router.get(`/${routeParts[1]}/${routeParts[2]}`, (req, res) => {
    res.json({ message: `You are accessing the ${routeParts[1]}/${routeParts[2]} endpoint` });
  });

  // Return the router
  return router;
}