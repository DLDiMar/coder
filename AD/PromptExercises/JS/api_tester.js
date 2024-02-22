const createApiRouter = require('./createApiRouter');

const express = require('express');
const app = express();

const testRouter = createApiRouter('main/follows/subscribers');
app.use('/api', testRouter);

const PORT = 3300;

app.listen(PORT, () => {
  console.log(`Server is running on http://localhost:${PORT}`);
});
