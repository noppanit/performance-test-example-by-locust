Getting Started
==================================

This example shows how can you get started with Locust and write the results to a file. So you can keep the file in an artifact in CI for future reference. You can do pretty much anything with the results. 


What you need
==================================

```
pip install locustio
```

```
locust --no-web -c 10 -r 1 -n 10 --only-summary --print-stats
```

