# Warm-up

For this warm-up, let's work with the [**Open Graph** protocol](https://ogp.me/).

First, we will implement a Python function in a `.py` file.

Then we will use that function in a Notebook.

## What is OpenGraph?

Ever shared a URL on Facebook, Twitter, Linkedin? You usually get a nice picture with a title + a description. For instance, type `https://www.lewagon.com` in [metatags.io](https://metatags.io/) to get a preview.

How does it work? These social networks + this tool will perform an HTTP request to the URL, and parse the HTML. In that HTML, they will find the following tags in `<head />`:

```html
<meta property="og:site_name" content="Coding Bootcamp Le Wagon | Most Acclaimed Coding Bootcamp Worldwide">
<meta property="og:type" content="article">
<meta property="og:url" content="https://www.lewagon.com/" />
<meta property="og:image" content="https://dwj199mwkel52.cloudfront.net/assets/core/social/home-card-82f54b75841da25d31c2e99d673e68152942dfd3d7275380508a63f0d951b484.jpg" />
```

They use that information to build the card.

## API

The goal of this challenge is not to scrape the website looking for the `<meta />` tags (even if that could be interesting to do!). We will use a Le Wagon API which does the heavy lifting for you. The API is hosted at [https://opengraph.lewagon.com](https://opengraph.lewagon.com).

👉 Check the API's documentation here: [github.com/lewagon/opengraph](https://github.com/lewagon/opengraph#readme)

Use `curl` or your browser to perform a few requests and have a look at the JSON returned by the API. If you have a hard time reading the documentation and making sense of it, please _make a ticket_ so a TA can help! Do not get stuck here.

## Python File

Open the `opengraph.py` file in VS Code. You will find an empty `fetch_metadata` function that you need to implement.

These are the requirements:

- This function takes a `url` parameter and, using the [`requests`](https://requests.readthedocs.io/en/master/) package, will retrieve Open Graph metadata of the specified url + return them as a dictionary.
- If for some reason the API returns an error (for example HTTP status code `404` or `422` or `500`, basically anything that is not `200`), then the function should return an empty `dict`.

This function implementation is about 4 lines of Python, please _make a ticket_ if you are stuck at this step. You'll know you're done with this file when `make` passes the first 5 tests, don't hesitate to commit that checkpoint!

> Note, that our API is using [a Ruby gem](https://github.com/jcouture/ogp) (think "pip package for Ruby"), which validates that certain meta-tags exist in a URL and returns an error otherwise. If you want to know which meta-tags it requires, check [the documentation](https://github.com/jcouture/ogp#attribute-validation).

Once you've implemented the `fetch_metadata` function, make sure to test and commit to GitHub! (At this point, make should pass 5 out of 6 tests.)


```bash
make

git add opengraph.py
git commit -m "Implemented fetch_metadata using https://github.com/lewagon/opengraph API"
git push origin master
```

## Notebook

Time to use the `fetch_metadata` function in a Notebook context!

```bash
jupyter notebook Warmup.ipynb
```

When you are done with the notebook, check whether **`make` is 100% green** and if yes commit and push your work:

```bash
git add opengraph.py Warmup.ipynb urls.csv
git commit -m "Load URLs from CSV and programatically fetch Open Graph information"
git push origin master
```
