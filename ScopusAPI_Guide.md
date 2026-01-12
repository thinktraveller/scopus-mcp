# Elsevier Scopus APIs

# Getting Started Guide

Version 1

Version 1

Date September 2023

# Version history

<table><tr><td>Version</td><td>Date</td><td>Author</td><td>Changes</td></tr><tr><td>1</td><td>September 2023</td><td>-</td><td>Initial publication</td></tr></table>

# Table of Contents

Introduction. 5

1. Overview of Scopus APIs 6  
2. Authenticate 8

2.1. IP-based authentication 8  
2.2. Institutional token authentication 9  
2.3. Access and entitlement 9  
2.4. Off-platform data requests 10

3. Request 11

3.1. Root-endpoint 12  
3.2. Headers 12  
3.3.Method 13  
3.4. Query parameters 13  
3.5.Faceting and sorting 13

4. Response 15

4.1. Request and response examples 16

5. Abstract Retrieval API 27

5.1. Interfaces and views 27  
5.2. API-specific query parameter options 29  
5.3.Note about "dummy" records 29

6. Abstract Citation Count API 30

6.1. Interfaces and views 30  
6.2. API-specific query parameter options 30

7. Citation Overview API 31

7.1. Interfaces and views 31  
7.2. API-specific query parameter options 32

8. Serial Title API 33

8.1. Interfaces and views 33  
8.2. API-specific query parameter options 34

9. Subject Classifications API 35

9.1. Interfaces 35  
9.2. API-specific query parameter options 35

10. Affiliation Retrieval API 36

10.1. Interfaces and views 36  
10.2. API-specific query parameter options 38

11. Author Retrieval API 39

11.1. Interfaces and views 39  
11.2. API-specific query parameter options.. 41

12. PlumX Metrics API 42

12.1. Interfaces 42  
12.2. API-specific template and query parameter options 42

13. Affiliation Search API 43

13.1. Interfaces and views 43  
13.2. API-specific query parameter options.. 44

14. Author Search API 45

14.1. Interfaces and views 45  
14.2. API-specific query parameter options.. 46

15. Scopus Search API 47

15.1. Interfaces and views 47  
15.2. API-specific query parameter options.. 49

16.Description of query parameters 50  
17. Description of elements associated with Abstracts included in a response 54  
18.Description of elements associated with Author included in a response 61  
19. Description of elements associated with Affiliation included in a response 63

# Introduction

Elsevier's Scopus Application Programming Interfaces (APIs) grant programmatic access to the curated abstracts and citation data from all scholarly journals indexed by Scopus. Each of the 11 APIs return different data to support a range of different use cases, including:

- Automatically display publication, citation, and author metrics on institution platforms  
- Conduct federated searches and analyze publication dynamics  
- Populate current research information systems (CRIS)  
Benchmark research performance and identify research trends

Scopus APIs can be used with any tool and/or programming language. This user guide explains how to retrieve data via the Scopus APIs.

![](images/585502b6b92646984f61309950599fb1bfb67b010709e6dde871f9ea0b5fb880.jpg)

Visit the following link for a collection of different use cases and details about their implementation: Scopus API use cases

# 1. Overview of Scopus APIs

Eleven APIs grant access to Scopus content. Eight are designed to retrieve metadata, content, metrics and other data from specified Scopus document, author profile, and affiliation profile records. The remaining three enable searches within the Scopus body of abstracts, author profiles, and affiliation profiles. Some of the APIs have more than one "view" in which responses are returned. Those views differ in the content fields they include and may be restricted based on `access or entitlement`.

<table><tr><td>API</td><td>Description and Root-endpoint</td><td>Method</td><td>Multiple views</td><td>Response formats</td></tr><tr><td rowspan="2">Abstract Retrieval</td><td>Returns the Scopus abstracts of a specified document, including rich metadata like links to author and affiliation profiles.</td><td rowspan="2">GET</td><td rowspan="2">●</td><td rowspan="2">XML</td></tr><tr><td>https://api.elsevier.com/content/abstract</td></tr><tr><td rowspan="2">Abstract Citation Count</td><td>Returns citation (cited by) counts for specified documents as a Scopus-branded image or metadata.</td><td rowspan="2">GET</td><td rowspan="2"></td><td rowspan="2">JPG JSON XML</td></tr><tr><td>https://api.elsevier.com/content/abstract/citation-count</td></tr><tr><td rowspan="2">Citation Overview</td><td>Returns citation metadata, including counts and citation summaries, for specified documents.</td><td rowspan="2">GET</td><td rowspan="2"></td><td rowspan="2">JSON XML</td></tr><tr><td>https://api.elsevier.com/content/abstract/citations</td></tr><tr><td rowspan="2">Serial Title</td><td>Returns metadata, including journal metrics, or cover image of one or more specified serial titles.</td><td rowspan="2">GET</td><td rowspan="2">●</td><td rowspan="2">GIF JSON XML</td></tr><tr><td>https://api.elsevier.com/content/serial/title</td></tr><tr><td rowspan="2">Subject Classifications</td><td>Returns subject classifications used in Scopus or ScienceDirect content.</td><td rowspan="2">GET</td><td rowspan="2"></td><td rowspan="2">JSON XML</td></tr><tr><td>https://api.elsevier.com/content/subject</td></tr><tr><td rowspan="2">Affiliation Retrieval</td><td>Returns a Scopus affiliation profile, which may contain links to Scopus Search and author profiles.</td><td rowspan="2">GET</td><td rowspan="2">●</td><td rowspan="2">JSON ATOM XML</td></tr><tr><td>https://api.elsevier.com/content/affiliation</td></tr><tr><td rowspan="2">Author Retrieval</td><td>Returns one ore more Scopus author profiles, which may contain links to Scopus Search and affiliation profiles.</td><td rowspan="2">GET</td><td rowspan="2">●</td><td rowspan="2">JSON ATOM XML</td></tr><tr><td colspan="1">https://api.elsevier.com/content/author</td></tr><tr><td rowspan="2">PlumX Metrics</td><td>Returns PlumX metrics (aggregate metric counts) for a specified document.</td><td rowspan="2">GET</td><td rowspan="2">●</td><td rowspan="2">JSON ATOM XML</td></tr><tr><td colspan="1">https://api.elsevier.com/analytics/plumx</td></tr><tr><td rowspan="2">Affiliation Search</td><td>Allows searching the Scopus affiliation profiles. Each result will include a link to an affiliation profile.</td><td rowspan="2">GET</td><td rowspan="2"></td><td rowspan="2">JSON ATOM XML</td></tr><tr><td colspan="1">https://api.elsevier.com/content/search/affiliation</td></tr><tr><td rowspan="2">Author Search</td><td>Allows searching the Scopus author profiles. Each result will include a link to an author profile and lay include a link to the author's current affiliation profile.</td><td rowspan="2">GET</td><td rowspan="2"></td><td rowspan="2">JSON ATOM XML</td></tr><tr><td colspan="1">https://api.elsevier.com/content/search/author</td></tr><tr><td rowspan="2">Scopus Search</td><td>Allows searching Scopus abstracts. Each result will link to a Scopus abstract and may include a link to the full-text article.</td><td rowspan="2">GET</td><td rowspan="2">●</td><td rowspan="2">JSON ATOM XML</td></tr><tr><td colspan="1">https://api.elsevier.com/content/search/scopus</td></tr></table>

![](images/115092f925a92624baa1832b93827fef2fe4e6931b7e1f98790fba37afa377ad.jpg)

Additional information and specifications can be found at:

Elsevier Developer Portal Documentation: Scopus API Specification

For support, visit the dedicated online developer portal at https://dev.elsevier.com

Alternatively, send an e-mail to apisupport@elsevier.com

# 2. Authenticate

An application that uses one or more Scopus APIs must use a unique caller name known as an API Key to identify itself. This API Key cannot be reused for another application. Elsevier provides two authentication methods to request an API, both requiring an API Key.

- Institution IP-based authentication access  
- Institutional token authentication

To obtain an API Key and gain access to a Scopus API, visit:

Register for an APIKey

To learn more about API Keys and authentication, visit:

- API Technical Specifications  
- API Authentication

# 2.1. IP-based authentication

The IP-based method is the default for any Scopus API Key and is meant for institutional subscribers that use IP authentication to access Scopus. The same IP addresses registered by an institution with Elsevier to access the Scopus web interface can be used to access the Scopus APIs. Run your application on an internet-enabled machine with a registered IP address and use your API Key to authenticate each request to the Scopus APIs. You can authenticate by submitting your API Key as an http request header (recommended for security):

curl -X GET --header 'Accept: text/xml' 'https://api.elsevier.com/content/abstract/doi/10.1016/S0014-5793(01)03313-0?apiKey=[Your API Key]'

curl -X GET --header 'Accept: text/xml' 'https://api.elsevier.com/content/search/author query=authlast(Einstein)%20and%20authfirst(Albert)%20and%20affil(Princeton)&apiKey=[Your API Key]'

# Or within a request URL:

http://api/elsevier.com/content/abstract/doi/10.1016/S0014-5793(01)03313-0?apiKey=[Your API Key]

http://api.elsevier.com/content/search/author?query=authlast(Einstein)%20and%20authfirst(Albert)%20and%20affil(Princeton)& apiKey=[Your API Key]

# 2.2. Institutional token authentication

An institutional token, or instttoken, is an additional security token submitted in tandem with your API Key. Insttokens are only available for customers or partners working on behalf of a customer that cannot use IP authentication to access the Scopus APIs and thus, must be enabled manually by an Elsevier representative to use an API Key. An institutional token gives full access to the customer account within Elsevier authentication and entitlements system. If you are granted an instttoken, Elsevier provides additional details about restrictions and use.

# 2.3. Access and entitlement

Access and entitlement varies according to user. Non-subscribers have limited access to some Scopus APIs, like the BASIC view of the Scopus Search and the Abstract Retrieval APIs. Academic subscribers have access to most Scopus APIs and data fields under their subscription to the Scopus web interface. Finally, commercial customers have access to Scopus APIs and data fields as defined in API-specific licenses.

While most Scopus APIs and data fields are automatically available to institutions with a valid Scopus subscription, some Scopus APIs, data fields, and results views are only available upon request. For access, use your institution e-mail to send a request via the following link. Include your API Key and use case.

![](images/940949a9ba0ef6099b10fd3ac513e71252aeffd261d35aa0cbcefb94b28ab4f0.jpg)

Visit the following link to request an access-controlled API or permission: Data as a Service Support Center

Access-controlled Scopus APIs and permissions that are available only upon request include:

Citation Overview API  
refEID field  
- Index Keyword field  
- DOCUMENTS view of the Affiliation Retrieval and Author Retrieval APIs

Please note that our policy is to enable special access on only one API Key per project. Quotas are then adjusted accordingly to meet the needs of that project.

# 2.4. Off-platform data requests

Third-party providers working with international repositories or CRIS systems may request access to Scopus APIs. In that case, a Customer Consultant is asked to submit an Off-Platform Data Request (OPDR) form. Access is granted upon approval by the OPDR team.

# 3. Request

An API URL is called a request while the data sent back to you is called a response.

A request consists of four components:

- Root-endpoint (or route)  
- Headers  
Method  
- Query parameters

Access to a Scopus API has a rate limit (throttling); that is, a maximum number of requests per second. Each API Key created is assigned a throttling level of Development, Low, Medium or High according to user needs. The rate limit corresponding to each level depends on the API. API Keys are also assigned a default weekly quota, but these can be individually defined for an API Key. The following table summarizes the default quotas of the Scoups APIs. The APIs return an http 429 TOO MANY REQUESTS message when a quota or throttle rate is exceeded.

<table><tr><td colspan="7">Rate limits</td></tr><tr><td>API name</td><td>Result limits</td><td>Development</td><td>Low</td><td>Medium</td><td>High</td><td>Weekly quota</td></tr><tr><td>Abstract Retrieval</td><td>-</td><td>9</td><td>9</td><td>12</td><td>15</td><td>10,000</td></tr><tr><td>Abstract Citations Count</td><td>Default 25 results; maximum 200 results</td><td>15</td><td>15</td><td>20</td><td>20</td><td>20,000</td></tr><tr><td>Serial Title</td><td>Default 25 results; maximum 200 results</td><td>6</td><td>6</td><td>9</td><td>12</td><td>20,000</td></tr><tr><td>Subject Classifications</td><td>Default 25 results; maximum 200 results</td><td>N/A</td><td>N/A</td><td>N/A</td><td>N/A</td><td>N/A</td></tr><tr><td>Affiliation Retrieval</td><td>-</td><td>9</td><td>9</td><td>12</td><td>15</td><td>5,000</td></tr><tr><td>Author Retrieval</td><td>-</td><td>6</td><td>6</td><td>9</td><td>12</td><td>5,000</td></tr><tr><td>Affiliation Search</td><td>Default 25 results; maximum 200 results; 5,000 item result limit</td><td>6</td><td>6</td><td>9</td><td>12</td><td>5,000</td></tr><tr><td>Author Search</td><td>Default 25 results; maximum 200 results; 5,000 item result limit</td><td>6</td><td>6</td><td>9</td><td>12</td><td>5,000</td></tr><tr><td>Scopus Search</td><td>Maximum 25–200 results, depending on view; 5,000 item result limit without &#x27;cursor pagination&#x27;</td><td>9</td><td>9</td><td>12</td><td>15</td><td>20,000</td></tr></table>

![](images/b9669d756b10d8366fe0feed52039790d1baed23486f2c91c82874652545b1ee.jpg)

Visit the following link for additional information on quotas:

How much data can I retrieve with my API Key?

To request a quota increase, submit an email via the following link:

Data as a Service Support Center

# 3.1. Root-endpoint

The root-endpoint is the starting point of each Scopus API to which you are placing a request. The root-endpoint of each Scopus API is listed in the table on page 6. A request consists of the root-endpoint followed by query parameters.

For example, the request URL in the Scopus Search API for a simple query of the term "diabetes" and specifying XML output would look something like this:

https://api/elsevier.com/content/search/scopus?http:paccept  $\equiv$  application/xml&query  $\equiv$  diabetes

&apiKey=[Your API Key]

# 3.2. Headers

The Headers interface of the API allows you to perform various actions on http request and response headers. For the purposes of this guide, we will use the command line utility curl.

Make sure you have curl installed. Type the following command in your system terminal to check the version installed on your system:

Curl --version

Type curl followed by the header parameters you wish to include and then the root-endpoint you're requesting. In the case of the request above:

curl -X GET --header 'Accept: application/xml' 'https://api.elsevier.com/content/search/scopus?query=diabetes

&apiKey=[YourAPIKey]'

Accept is a required parameter. Other header parameters serve to provide access and authorization information.

<table><tr><td>Header parameter</td><td>Description</td></tr><tr><td>Accept</td><td>(required) Indicates format of the data download. Options include application/xml, application/json, application/atom+xml, text/xml, text/html. The Citation Count API also has the option image/jpeg, and Serial Title API has the option of image/gif.</td></tr><tr><td>Authorization</td><td>Contains an OAuth bearer token to place requests executed against user-based entitlements. Overrides X-ELS-Authtoken.</td></tr><tr><td>X-ELS-APIKey</td><td>Contains the unique application developer key.</td></tr><tr><td>X-ELS-Authtoken</td><td>Key to validate credentials to access a resource for an end-user session.</td></tr><tr><td>X-ELS-ReqId</td><td>Contains a client-defined request identifier that is logged in all trace messages of the service. Used to track specific transactions.</td></tr><tr><td>X-ELS-Insttokens</td><td>Contains an institution token provided in combination with the associated API Key to establish credentials for resource access.</td></tr><tr><td>X-ELS-ResourceVersion</td><td>Indicates the version of the resource that should be used.</td></tr></table>

# 3.3. Method

The method is the type of request you send to the server. All Scopus APIs use the GET method.

# 3.4. Query parameters

The last part of the request URL lists the query parameters. Query parameters begin with a question mark (?) and each subsequent parameter pair is separated by an ampersand (&). See page 50 for a list and description of query parameters available in each API.

# 3.5. Faceting and sorting

The Affiliation Search, Author Search, and Scopus Search APIs include a query parameter called facets. It is used to define data fields for the faceted navigation of records in a response.

One or more fields can be defined for faceting. They should be separated by a semicolon. Each facet can also be modified along the dimensions listed in the table below, which are entered in parentheses after the facet, separated by commas.

facets=prefnameauid(count=20,sort=na,prefix=Ma);exactsrtitle(prefix=J);subjabbr(range=fd);pubyr;exactkeywordword(count=fdna)

<table><tr><td>Facet dimension</td><td>Description</td></tr><tr><td>count</td><td>Defines the number of „ buckets“ to include in a facet.</td></tr><tr><td>sort</td><td>Indicates how the facet categories should be sorted. Options include “na” by category name, ascending; “fd” by category frequency, descending; and “fdna” by category frequency descending, secondary sort by name ascending.</td></tr><tr><td>prefix</td><td>Filters the facet values to only those matching a specific prefix (not applicable to numerical values).</td></tr></table>

Furthermore, you can include or exclude certain values from a faceted response using the qualifiers listed in the table below. These facet qualifiers (include, exclude, and variations thereof) can only be included if the prefix parameter is also part of the request.

<table><tr><td>Facet qualifier</td><td>Description</td></tr><tr><td>include</td><td>Includes in the faceted response only the value specified.</td></tr><tr><td>include_above</td><td>Includes in the faceted response only values above the value specified.</td></tr><tr><td>includebelow</td><td>Includes in the faceted response only values below the value specified.</td></tr><tr><td>exclude</td><td>Excludes the value specified from the faceted response.</td></tr><tr><td>exclude_above</td><td>Excludes values above the value specified from the faceted response.</td></tr><tr><td>Excludebelow</td><td>Excludes values below the value specified from the faceted response.</td></tr></table>

Another query parameter called sort that is available in the three Search APIs and in the Citation Overview API allows defining fields by which records in a response are sorted.

Entry options for the facets and sort query parameters differ among the APIs. The options are listed and defined in the chapters corresponding to each API.

Some examples of requests and their corresponding responses can be found on page 16.

# 4. Response

The response to a request is returned in the format defined either in the header parameter Accept or the query parameter httpAccept. Options include XML, JSON, or an image.

Responses are limited to a finite number of records, defined by the contracted service level and/or entitlements. Loop over the response using start and count to retrieve batches of records in a response. For example, the following request delivers records 200 to 399 of the response.

https://api/elsevier.com/content/search/scopus?start=200&count=200&httpaccept  $\equiv$  application/xml&query  $\equiv$  diabetes&APIKey  $\equiv$  [YourAPIKey]

![](images/f1074f5be3af944809fc8cdba6d109efa2a4dc3090e24e41fe0aae53bf0e7575.jpg)

A response is limited to a predefined number of records. However, you can computationally loop over the response to download the complete set of data.

Retrieval of large data sets (>100,000 records) is discouraged. Download gets progressively slower at the tail end of the data set and causes high server load. Single requests can be apportioned, for example by publication year, to generate several smaller data sets. Note that the number of requests placed to a given API is also restricted by a quota and throttle rate.

Each response is also returned with a standardized message about the status of the request.

# Response Messages

<table><tr><td>HTTP Status Code</td><td>Reason</td><td>HTTP Status Code</td><td>Reason</td></tr><tr><td>400</td><td>Invalid information submitted</td><td>200</td><td>OK</td></tr><tr><td>401</td><td>Missing/invalid credentials</td><td>300</td><td>Single author profile is superseded by multiple author profiles</td></tr><tr><td>403</td><td>Authentication or entitlements cannot be validated</td><td>301</td><td>Redirection to a superseding single author profile</td></tr><tr><td>404</td><td>Requested resource not found</td><td>429</td><td>Quota exceeded</td></tr><tr><td>405</td><td>Invalid http method</td><td>500</td><td>Generic error</td></tr><tr><td>406</td><td>Invalid mime type</td><td></td><td></td></tr></table>

# 4.1. Request and response examples

The following are examples of requests that can be made with the Scopus APIs. Where possible, we've included the full or abridged response. Note that the sample responses are limited to content in Scopus as of the publication date of this User Guide. Scopus content is continually updated, so responses may deviate.

![](images/d10f7e4e600c5512f3872036536902b6369412989e5c79d8fd35a2b7732929a7.jpg)

Use the interactive APIs to experiment with requests and responses.

Scopus Interactive APIs

# Example 1: Scopus Citation Overview API

Intent: To retrieve citation counts for a document (Scopus ID: 33646008552) broken down by year and excluding self-citations.

# Request:

https://api.elsevier.com/content/abstract/citations?scopus_id=33646008552&citation  $\equiv$  exclude-self

# Example 2: Scopus Abstract Citation Count API

Intent: To retrieve the citation counts of a document (doi: 10.1590/1519-6984.250236) as metadata.

# Request:

```txt
https://api.elsevier.com/content/abstract/citation-count?doi=10.1590/1519-6984.250256&httpAccept  $\equiv$  application ion/xml
```

# Response:

```xml
<?xml version="1.0" encoding="utf-8"?>
<citation-count-response xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:prism="http://prismstandard.org/namespaces/basic/2.0/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
    <document status="found">
        <dc:identifier>SCOPUS_ID:85123025187</dc:identifier>
        <prism:url>https://api.elsevier.com/content/abstract/scopus_id/85123025187</prism:url>
        <prism:doi>10.1590/1519-6984.250256</prism:doi>
        <pii />
        <pubmed_id>34932624</pubmed_id>
        <eid>2-s2.0-85123025187</eid>
        <article-number>e250256</article-number>
        <citation-count>9</citation-count>
        <link href="https://www.scopus.com/inward/record.uri?partnerID=HzOxMe3b&amp;scp=85123025187&a
mp;origin=inward" rel="scopus" />
        <link href="https://www.scopus.com/inward/citedby.uri?partnerID=HzOxMe3b&amp;scp=85123025187&a
mp;origin=inward" rel="scopus-citedby" />
        </document>
        </citation-count-response >
```

# Example 3: Scopus Serial Title API

Intent: Retrieve the cover image (first request) and the metadata (second request) of a serial title (ISSN: 03088146), including journal metrics like IPP, SJR, and SNIP.

# Request (cover image):

```txt
https://api.elsevier.com/content/serial/title/issn/03088146?view=coverimage
```

# Request (metadata):

```txt
https://api.elsevier.com/content/serial/title/issn/03088146
```

Response (metadata):  
```jsonl
{
"serial-meta-data-response":{ "link":[ { "@_fa": "true", "@ref": "self", "@href": "https://api.elsevier.com/content/serial/title/issn/03088146", "@type": "application/json" } ], "entry": [ { "@_fa": "true", "dc:title": "Food Chemistry", "dc:publisher": "Elsevier Ltd.", "coverageStartYear": "1976", "coverageEndYear": "2023", "prism:aggregationType": "journal", "source-id": "24039", "prism:issn": "0308-8146", "prism:elssn": "1873-7072", "openaccess": "0", "openaccessArticle": false, "openArchiveArticle": false, "openaccessType": "None", "openaccessStartDate": null, "oaAllowsAuthorPaid": false, "subject-area": [ { "@_fa": "true", "@code": "1602", "@abbrev": "CHEM", "$": "Analytical Chemistry" }, { "@_fa": "true", "@code": "1106", "@abbrev": "AGRI", "$": "Food Science" } ], "SNIPList":{ "SNIP":[ { "@_fa": "true", "@year": "2022", "$": "2.197" } ] }, "SJRList":{
```

```jsonl
"SJR": [ { "@_fa": "true", "@year": "2022", "$": "1.624" } ] }, "citeScoreYearInfoList": { "citeScoreCurrentMetric": "14.9", "citeScoreCurrentMetricYear": "2022", "citeScoreTracker": "12.6", "citeScoreTrackerYear": "2023" }, "link": [ { "@_fa": "true", "@ref": "scopus-source", "@href": "https://www.scopus.com/source/sourceInfo.url?sourceId=24039" }, { "@_fa": "true", "@ref": "homepage", "@href": "http://www.sciencedirect.com/science/journal/03088146" }, { "@_fa": "true", "@ref": "coverimage", "@href": "https://api.elsevier.com/content/serial/title/issn/0308-8146?view=coverimage" } ], "prism:url": "https://api.elsevier.com/content/serial/title/issn/0308-8146" } }
```

# Example 4: Scopus Subject Classifications API

Intent: To list subject classifications associated with with Scopus content.

# Request:

https://api.elsevier.com/content/subject/scopus

# Response (abridged):

<?xml version="1.0" encoding="UTF-8"?>

<object-classifications>

<subject-classification code="1000" detail="Multidisciplinary" abbreviation="MULT">Multidisciplinary</subject-classification>

<subject-classification code="1100" detail="Agricultural and Biological Sciences (all)" abbreviation="AGRI">Agricultural and Biological Sciences</subject-classification>

<subject-classification code="1101" detail="Agricultural and Biological Sciences (miscellaneous)" abbrev="AG RI">Agricultural and Biological Sciences</subject-classification>

<subject-classification code="1102" detail="Agronomy and Crop Science" abbrev="AGRI">Agricultural and Biological Sciences</subject-classification>

<subject-classification code="1103" detail="Animal Science and Zoology" abbreviation="AGRI">Agricultural and Biological Sciences</subject-classification>

<subject-classification code="1104" detail="Aquatic Science" abbrev="AGRI">Agricultural and Biological Sciences</subject-classification>

<subject-classification code="1105" detail="Ecology, Evolution, Behavior and Systematics" abbrev="AGRI">Agricultural and Biological Sciences</subject-classification>

[...]

<subject-classification code="3616" detail="Speech and Hearing" abbreviation="HEAL">Health Professions</subject-classification>

</subject-classifications>

# Example 5: Scopus Abstract Retrieval API

Intent: To retrieve the full abstract and metadata (including links to author and affiliation profiles) of a document (doi: 10.1002/ajp.23170).

# Request:

https://api.elsevier.com/content/abstract/doi/10.1002/ajp.23170

# Example 6: Scopus Author Retrieval API

Intent: To retrieve the Scopus author profile with Scopus Author ID 56962745700 plus metadata. Note: Scopus author profiles are indexed and can be searched with the Author Search API.

# Request:

https://api.elsevier.com/content/author/author_id/56962745700

# Example 7: Scopus Affiliation Retrieval API

Intent: To retrieve the Scopus affiliation profile with Scopus Affiliation ID 60090656 plus metadata. Note: Scopus affiliation profiles are indexed and can be searched with the Affiliation Search API.

# Request:

```txt
https://api/elsevier.com/content/search/affiliation?query=af-id(60090656)
```

# Response:

```jsonl
{
    "search-results": {
        "opensearch:totalResults": "1",
        "opensearch:startIndex": "0",
        "opensearch:itemsPerPage": "1",
        "opensearch:Query": {
            "@role": "request",
            "@searchTerms": "af-id(60090656)", "@startTime": "0"
        },
    }
    "link": [
        [
            "@_fa": "true",
            "@ref": "self",
            "@href": "https://api.elsevier.com/content/search/affiliation?start=0&count=25&query=af-id%2860090656%29",
            "@type": "application/json"
        ],
        [
            "@_fa": "true",
            "@ref": "first",
            "@href": "https://api.elsevier.com/content/search/affiliation?start=0&count=25&query=af-id%2860090656%29",
            "@type": "application/json"
        ]
    ],
    "entry": [
        {@_fa}: "true",
        "link": [
            {@_fa}: "true",
            @ref]: "self",
            @href?: "https://api.elsevier.com/content/affiliation/affiliation_id/60090656"
        ],
        {@_fa": "true",
            @ref": "search",
```

```jsonl
"@href": "https://api.elsevier.com/content/search/scopus?query  $\equiv$  af-id%2860090656%29"
\},
\{
	"@fa": "true",
	"@ref": "scopus-affiliation",
	"@href": "https://www.scopus.com/affil/profile.uri?afid=60090656&partnerID=HzOxMe3b&origin
=inward"
\}
\},
"prism:url": "https://api.elsevier.com/content/affiliation/affiliation_id/60090656",
"dc:identifier": "AFFILIATION_ID:60090656",
"eid": "10-s2.0-60090656",
"affiliation-name": "Universiti Tun Hussein Onn Malaysia",
"name-variant": [ \{
	"@fa": "true",
	"\$" : "Universiti Tun Hussein Onn Malaysia"
\},
"document-count": "15978",
"city": "Batu Pahat",
"country": "Malaysia",
"parent-affiliation-id": "0"
\}
\}
\}
```

# Example 8: Scopus Search API

Intent: To list all Scopus abstract entries that include heart attack in the title, published between 2018 and 2020. Entries should be provided in the COMPLETE view.

# Request:

```txt
https://api.elsevier.com/content/search/scopus?query  $\equiv$  PUBYEAR  $^+$  %3E+2018+AND+PUBYEAR  $^+$  %3C+2020+AND $\% 28\text{TITLE}\% 28\text{heart} +$  attack%29%29&view  $\equiv$  complete
```

# Example 9: Scopus Affiliation Search API

Intent: To retrieve any Scopus affiliation profiles (including metadata) for the University of Washington.

# Request:

```txt
https://api.elsevier.com/content/search/affiliation?query=AFFIL(University of Washington)
```

# Example 10: Scopus Author Search API

Intent: To retrieve the Scopus author profile (including metadata) with the Scopus Author ID 55547104688.

# Request:

```txt
https://api.elsevier.com/content/search/author?query=au-id(55547104688)
```

# Response:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<search-results xmlns="http://www.w3.org/2005/Atom" xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:op
ensearch="http://a9.com-/spec/opensearch/1.1/" xmlns:prism="http://prismstandard.org/namespaces/basic/2
.0/" xmlns:atom="http://www.w3.org/2005/Atom">
    <opensearch:totalResults>1</opensearch:totalResults>
    <opensearch:startIndex>0</opensearch:startIndex>
    <opensearch:itemsPerPage>1</opensearch:itemsPerPage>
    <opensearch:Query role="request" searchTerms="au-id(55547104688)" startPage="0"/> 
    <link ref="self" href="https://api/elsevier.com/content/search/author?start=0&count=25&query=a
u-id%2855547104688%29" type="application/xml"/> 
    <link ref="first" href="https://api/elsevier.com/content/search/author?start=0&query=25&query=a
u-id%2855547104688%29" type="application/xml"/> 
    <entry>
        <link ref="self" href="https://api/elsevier.com/content/author/author_id/55547104688"/> 
        <link ref="search" href="https://api/elsevier.com/content/search/author?query=au-id%2855547104688%2
9"/> 
        <link ref="scopus-citedby" href="https://www.scopus.com/author/citedby.uri?partnerID=HzOxMe3b&amp;
citedAuthorld=55547104688&amp;origin=inward"/> 
        <link ref="scopus-author" href="https://www.scopus.com/athid/detail.uri?partnerID=HzOxMe3b&amp;au
thorld=55547104688&amp;origin=inward"/> 
    <prism:url>https://api/elsevier.com/content/author/author_id/55547104688</prism:url>
    <dc:identifier>AUTHOR_ID:55547104688</dc:identifier>
    </preferred-name>
    < surname>Smith</ surname>
    <given-name>David E.</given-name>
    <initials>D.E.</initials>
    </preferred-name>
    <name-variant>
        <surname>Smith</ surname>
        <given-name>D. E.</given-name>
        <initials>D.E.</initials>
    </name-variant>
    <name-variant>
        < surname>Smith</ surname>
        <given-name>David E.</given-name>
        <initials>D.E.</initials>
    </name-variant>
    <name-variant>
        < surname>Smith</ surname>
        <given-name>David E.</given-name>
        <initials>D.E.</initials>
    </name-variant>
    <name-variant>
        < surname>Smith</ surname>
        <given-name>David E.</given-name>
        <initials>D.E.</initials>
    </ name-variant>
    <name-variant>
        < surname>Smith</ surname>
        <given-name>David E.</given-name>
        <initials>D.E.</initials>
    </name-variant>
    <name-variant>
        < surname>Smith</ surname>
        <given-name>David E.</given-name>
        <initials>D.E.</initials>
    </name-variant>
    <name-variant>
        < surname>Smith</ surname>
       <given-name>David E.</given-name>
       <initials>D.E.</initials>
    </name-variant>
    <name-variant>
        < surname>Smith</ surname>
       <given-name>David E.</given-name>
       <initials>D.E.</initials>
    </name-variant>
    <name-variant>
        < surname>Smith</ surname>
       <given-name>David E.</given-name>
       <initials>D.E.</initials>
    </name-variant>
    <(name-variant>
        < surname>Smith</ surname>
       <given-name>David E.</given-name>
       <initials>D.E.</initials>
    </name-variant>
    </name-variant>
</xml></xml>
```

```xml
<surname>Smith</surname>
<given-name>David A.</given-name>
<initials>D.A.</initials>
</name-variant>
<document-count>96</document-count>
<subject-area abbrev="EART" frequency="127">Earth and Planetary Sciences (all)</sub>/
<subject-area abbrev="PHYS" frequency="50">Physics and Astronomy (all)</sub>/
<subject-area abbrev="ENGI" frequency="24">Engineering (all)</sub>/
<affiliation-current>
  <affiliation?url>https://api.elsevier.com/content/affiliation/affiliation_id/60022195</affiliationurl>
  <affiliation-id>60022195</affiliation-id>
  <affiliation-name>Massachusetts Institute of Technology</affiliation-name>
  <affiliation-city>Cambridge</affiliation-city>
  <affiliation-country>United States</affiliation-country>
  </affiliation-current>
</entry>
</search-results>
```

# Example 11: PlumX API

Intent: To retrieve all PlumX metrics for the document with doi: 10.1103/physrevlett.116.061102

# Request:

https://api.elsevier.com/analytics/plumx/doi/10.1103/physrevlett.116.061102

# Response:

```json
{
    "id_type": "doi",
    "id_value": "10.1103/physrevlett.116.061102",
    "count_categories": [
        {
            "name": "capture",
            "total": 4754,
            "count_types": [
                "name": "READER_COUNT",
                "total": 4753
            ],
            "name": "EXPORTS_SAVES",
            "total": 1
        }
    ]
},
```

```txt
"total": 8658,   
"count_types": [ { "name": "CITED_BY_COUNT", "total": 8657, "sources": [ { "name": "Scopus", "total": 8657 }, { "name": "CrossRef", "total": 1409 }, { "name": "PubMed", "total": 181 }, { "name": "Academic Citation Index (ACI) - airiti", "total": 1 } ], { "name": "POLICY_CITED_BY_COUNT", "total": 1, "sources": [ { "name": "Policy Citation", "total": 1 } ] } ], { "name": "mention", "total": 435, "count_types": [ { "name": "REFERENCE_COUNT", "total": 193 }, { "name": "NEWS_COUNT", "total": 154 }, { "name": "QA Site MENTIONS", "total": 58 }, { "name": "ALL_BLOG_COUNT",
```

```jsonl
"total": 30   
}   
},   
{"name": "socialMedia", "total": 30752, "count_types": [ { "name": "FACEBOOK_COUNT", "total": 27032 }, { "name": "TWEET_COUNT", "total": 3720 } ] }, { "name": "usage", "total": 1992, "count_types": [ { "name": "LINKCLICK_COUNT", "total": 1704 }, { "name": "DOWNLOAD_COUNT", "total": 224 }, { "name": "ABSTRACT_VIEWS", "total": 59 }, { "name": "LINK_OUTS", "total": 5 } ] }
```

# 5. Abstract Retrieval API

Use the Abstract Retrieval API to request one or more Scopus abstracts using a document identifier, such as a DOI or PubMed ID. A full abstract includes rich metadata with links to author and affiliation profiles. Note that the native format of an abstract text is XML. Portions can be translated to JSON but the full abstract cannot be accurately represented in JSON format. The text of abstracts is searchable using the Scopus search API.

See page 20 for an example of a request.

# 5.1. Interfaces and views

Use the interface for the relevant document identifier to submit requests to the Abstract Retrieval API:

<table><tr><td>URL</td><td>Method</td><td>Description</td></tr><tr><td>https://api/elsevier.com/content/abstract/scopus_id/{scopus_id}</td><td>GET</td><td>Returns a Scopus abstract based on a Scopus Identifier.</td></tr><tr><td>https://api/elsevier.com/content/abstract/eid/{eid}</td><td>GET</td><td>Returns a Scopus abstract based on an Electronic Identifier.</td></tr><tr><td>https://api/elsevier.com/content/abstract/doi/{doi}</td><td>GET</td><td>Returns a Scopus abstract based on a Digital Object Identifier. Not every abstract record contains a DOI.</td></tr><tr><td>https://api/elsevier.com/content/abstract/pii/{pii}</td><td>GET</td><td>Returns a Scopus abstract based on a Publication Item Identifier. Not every abstract record contains a PII.</td></tr><tr><td>https://api/elsevier.com/content/abstract/pubmed_id/{pubmed_id}</td><td>GET</td><td>Returns a Scopus abstract based on a MEDLINE PubMed Identifier.</td></tr><tr><td>https://api/elsevier.com/content/abstract/pui/{pui}</td><td>GET</td><td>Returns a Scopus abstract based on an EMBASE Identification Number.</td></tr></table>

A textual metadata response is returned in one of five views based on access and entitlements: BASIC, META, META_ABS, REF, or FULL. The default view is META.

<table><tr><td>Parent field</td><td>Fields included</td><td>BASIC</td><td>META</td><td>META_ABS</td><td>REF</td><td>FULL</td></tr><tr><td></td><td>eid</td><td>•</td><td>•</td><td>•</td><td></td><td>•</td></tr><tr><td></td><td>link ref=scopus</td><td>•</td><td>•</td><td>•</td><td></td><td>•</td></tr><tr><td></td><td>prism:url</td><td>•</td><td>•</td><td>•</td><td>•</td><td>•</td></tr><tr><td></td><td>dc:identifier</td><td>•</td><td>•</td><td>•</td><td>•</td><td>•</td></tr><tr><td></td><td>openaccess</td><td>•</td><td>•</td><td>•</td><td></td><td>•</td></tr><tr><td></td><td>openaccessFlag</td><td>•</td><td>•</td><td>•</td><td></td><td>•</td></tr><tr><td></td><td>link ref= self</td><td></td><td>•</td><td>•</td><td></td><td>•</td></tr><tr><td></td><td>dc:title</td><td></td><td>•</td><td>•</td><td>•</td><td>•</td></tr><tr><td></td><td>prism:aggregationType</td><td></td><td>•</td><td>•</td><td></td><td>•</td></tr><tr><td></td><td>subtype</td><td></td><td>•</td><td>•</td><td></td><td>•</td></tr><tr><td></td><td>subtypeDescription</td><td></td><td>•</td><td>•</td><td></td><td>•</td></tr><tr><td></td><td>citedby-count</td><td></td><td>•</td><td>•</td><td>•</td><td>•</td></tr><tr><td></td><td>prism:publicationName</td><td></td><td>•</td><td>•</td><td>•</td><td>•</td></tr><tr><td></td><td>prism:ISBN</td><td></td><td>•</td><td>•</td><td></td><td>•</td></tr><tr><td></td><td>prism:issn</td><td></td><td>•</td><td>•</td><td></td><td>•</td></tr><tr><td></td><td>prism:volume</td><td></td><td>•</td><td>•</td><td>•</td><td>•</td></tr><tr><td></td><td>prism:issueldentifier</td><td></td><td>•</td><td>•</td><td>•</td><td>•</td></tr><tr><td></td><td>prism:pageRange</td><td></td><td>•</td><td>•</td><td>•</td><td>•</td></tr><tr><td></td><td>prism:coverDate</td><td></td><td>•</td><td>•</td><td></td><td>•</td></tr><tr><td></td><td>pubmed-id</td><td></td><td>•</td><td>•</td><td>•</td><td>•</td></tr><tr><td></td><td>prism:doi</td><td></td><td>•</td><td>•</td><td>•</td><td>•</td></tr><tr><td></td><td>article-number</td><td></td><td>•</td><td>•</td><td>•</td><td>•</td></tr><tr><td>dc:creator</td><td>@aubid</td><td></td><td>•</td><td>•</td><td></td><td>•</td></tr><tr><td></td><td>author_url</td><td></td><td>•</td><td>•</td><td></td><td>•</td></tr><tr><td>affiliation</td><td>affiliation-name</td><td></td><td>•</td><td>•</td><td></td><td>•</td></tr><tr><td>authors</td><td>author</td><td></td><td></td><td>•</td><td>•</td><td>•</td></tr><tr><td>author</td><td>@aubid</td><td></td><td></td><td>•</td><td>•</td><td>•</td></tr><tr><td></td><td>author_url</td><td></td><td></td><td>•</td><td>•</td><td>•</td></tr><tr><td>affiliation</td><td>afid</td><td></td><td></td><td>•</td><td></td><td>•</td></tr><tr><td></td><td>affiliation_url</td><td></td><td></td><td>•</td><td></td><td>•</td></tr><tr><td></td><td>dc:description</td><td></td><td></td><td>•</td><td></td><td>•</td></tr><tr><td></td><td>intid</td><td></td><td></td><td></td><td></td><td>•</td></tr><tr><td>subject-areas</td><td>subject-area</td><td></td><td></td><td></td><td></td><td>•</td></tr><tr><td>subject-area</td><td>@code</td><td></td><td></td><td></td><td></td><td>•</td></tr><tr><td></td><td>@abbrev</td><td></td><td></td><td></td><td></td><td>•</td></tr><tr><td>item</td><td>Label of original language</td><td></td><td></td><td></td><td></td><td>•</td></tr><tr><td></td><td>Author keywords</td><td></td><td></td><td></td><td></td><td>•</td></tr><tr><td></td><td>Index keywords (not available by default)</td><td></td><td></td><td></td><td></td><td>•</td></tr></table>

# 5.2. API-specific query parameter options

<table><tr><td>Query parameter</td><td>Options</td><td>Description</td></tr><tr><td rowspan="5">httpAccess</td><td>application/json</td><td>Sets mime type to JSON output; allows multiple records</td></tr><tr><td>application/xml</td><td>Sets mime type to XLM output; allows multiple records</td></tr><tr><td>application/rdf+xml</td><td>Sets mime type to RDF/XLM output; allows multiple records</td></tr><tr><td>text/xml</td><td>Sets mime type to XLM as text; allows multiple records</td></tr><tr><td>text/html</td><td>Sets mime type to html as text; allows multiple records</td></tr></table>

# 5.3. Note about "dummy" records

Records that are indexed in Scopus but do not include references, abstract and other metadata are called dummy records. Because they lack an abstract, such records generate a "Response Not Found" message in the Abstract Retrieval API. The records do, however, appear in results from the Scopus Search API. Because only core documents with all associated metadata within Scopus appear in responses from the Abstract Retrieval API, adding the parameter content=core to your request culls all "Response Not Found" messages.

# 6. Abstract Citation Count API

This API retrieves document citation counts as a watermarked image or as metadata in JSON or XML format. The image format is restricted to a single document and is considered a distinct resource, separate from a textual metadata response.

See page 17 for an example of a request.

# 6.1. Interfaces and views

A single interface is used to submit requests to the Abstract Citation Count API:

<table><tr><td>URL</td><td>Method</td><td>Description</td></tr><tr><td>https://api/elsevier.com/content/abstract/citation-count</td><td>GET</td><td>Returns the cited-by count of a document specified by an identifier.</td></tr></table>

A textual metadata response is returned in the default FULL view:

<table><tr><td>Fields included</td><td>FULL</td></tr><tr><td>prism:url</td><td>•</td></tr><tr><td>prism:doi</td><td>•</td></tr><tr><td>pii</td><td>•</td></tr><tr><td>pubmed_id</td><td>•</td></tr><tr><td>eid</td><td>•</td></tr><tr><td>citation-count</td><td>•</td></tr><tr><td>link rel=scopus</td><td>•</td></tr><tr><td>link ref=scopus-citedby</td><td>•</td></tr></table>

# 6.2. API-specific query parameter options

<table><tr><td>Query parameter</td><td>Options</td><td>Description</td></tr><tr><td rowspan="5">httpAccess</td><td>Image.jpeg</td><td>Sets mime type to a JPEG image</td></tr><tr><td>application/json</td><td>Sets mime type to JSON output; allows multiple records</td></tr><tr><td>application/xml</td><td>Sets mime type to XLM output; allows multiple records</td></tr><tr><td>text/xml</td><td>Sets mime type to XLM as text; allows multiple records</td></tr><tr><td>text/html</td><td>Sets mime type to html as text; allows multiple records</td></tr></table>

# 7. Citation Overview API

This API retrieves document citation counts for one or more specified documents broken down by year, with the option of excluding self-citations. It returns citation metadata, including counts and citation summaries. Use the Abstract Citation Count API to get total citation counts.

See page 16 for an example of a request.

# 7.1. Interfaces and views

A single interface is used to submit requests to the Citation Overview API:

<table><tr><td>URL</td><td>Method</td><td>Description</td></tr><tr><td>https://api.elsevier.com/content/abstract/citation</td><td>GET</td><td>Returns citation metadata, including counts and citation summaries.</td></tr></table>

A textual metadata response is returned in the default STANDARD view:

<table><tr><td>Parent field</td><td>Fields included</td><td>STANDARD</td></tr><tr><td rowspan="4">identifier</td><td>dc:identifier</td><td>●</td></tr><tr><td>prism:doi</td><td>●</td></tr><tr><td>pii</td><td>●</td></tr><tr><td>scopus_id</td><td>●</td></tr><tr><td></td><td>h-index</td><td>●</td></tr><tr><td colspan="3">The following fields are returned from the citelinfo entry of each document</td></tr><tr><td></td><td>dc:identifier</td><td>●</td></tr><tr><td></td><td>prism:url</td><td>●</td></tr><tr><td></td><td>dc:title</td><td>●</td></tr><tr><td rowspan="5">author</td><td>initials</td><td>●</td></tr><tr><td>index-name</td><td>●</td></tr><tr><td>surname</td><td>●</td></tr><tr><td>authid</td><td>●</td></tr><tr><td>author_url</td><td>●</td></tr><tr><td></td><td>sort-year</td><td>●</td></tr><tr><td></td><td>prism:publicationName</td><td>●</td></tr><tr><td></td><td>prism:volume</td><td>●</td></tr><tr><td></td><td>prism:issueIdentifier</td><td>●</td></tr><tr><td></td><td>prism:startingPage</td><td>●</td></tr><tr><td></td><td>prism:endingPage</td><td>●</td></tr><tr><td></td><td>prism:issn</td><td>●</td></tr><tr><td></td><td>citationType</td><td>●</td></tr><tr><td></td><td>pcc</td><td>●</td></tr><tr><td></td><td>cc</td><td>●</td></tr><tr><td></td><td>lcc</td><td>●</td></tr><tr><td></td><td>rangeCount</td><td>●</td></tr><tr><td></td><td>rowTotal</td><td>●</td></tr><tr><td colspan="3">The following fields are returned from the citeCountHeader summary</td></tr><tr><td></td><td>prevColumnHeader</td><td>●</td></tr><tr><td></td><td>columnHeading</td><td>●</td></tr><tr><td></td><td>laterColumnHeading</td><td>●</td></tr><tr><td></td><td>prevColumnTotal</td><td>●</td></tr><tr><td></td><td>columnTotal</td><td>●</td></tr><tr><td></td><td>laterColumnTotal</td><td>●</td></tr><tr><td></td><td>rangeColumnTotal</td><td>●</td></tr><tr><td></td><td>grandTotal</td><td>●</td></tr></table>

# 7.2. API-specific query parameter options

<table><tr><td>Query parameter</td><td>Options</td><td>Description</td></tr><tr><td rowspan="3">httpAccess</td><td>application/json</td><td>Sets mime type to JSON output; allows multiple records</td></tr><tr><td>application/xml</td><td>Sets mime type to XLM output; allows multiple records</td></tr><tr><td>text/xml</td><td>Sets mime type to XLM as text; allows multiple records</td></tr><tr><td rowspan="2">sort</td><td>sort-year</td><td>Sort results in response by year</td></tr><tr><td>rowTotal</td><td>Sort results in response by the sum of the pcc, lcc, and rangeCount fields</td></tr></table>

# 8. Serial Title API

This API allows searching through serial titles in the Scopus content and returning the metadata or cover image for a serial title identified by ISSN.

See page 17 for an example of a request.

# 8.1. Interfaces and views

The Serial Title API provides two interfaces:

<table><tr><td>URL</td><td>Method</td><td>Description</td></tr><tr><td>https://api/elsevier.com/content/serial/title</td><td>GET</td><td>To perform a search against the serial titles.</td></tr><tr><td>https://api/elsevier.com/content/serial/title/issn/{issn}</td><td>GET</td><td>Returns the metadata or cover image of a single serial title identified by ISSN.</td></tr></table>

A textual metadata response is returned in one of three views based on access and entitlements: BASIC, STANDARD, or ENHANCED. The default view is STANDARD.

<table><tr><td>Parent field</td><td>Fields included</td><td>BASIC</td><td>STANDARD</td><td>ENHANCED</td></tr><tr><td></td><td>openaccess</td><td>●</td><td>●</td><td>●</td></tr><tr><td></td><td>openaccessArticle</td><td>●</td><td>●</td><td>●</td></tr><tr><td></td><td>openArchiveArticle</td><td>●</td><td>●</td><td>●</td></tr><tr><td></td><td>openaccessType</td><td>●</td><td>●</td><td>●</td></tr><tr><td></td><td>openaccessStartDate</td><td>●</td><td>●</td><td>●</td></tr><tr><td></td><td>openaccessSponsorType</td><td>●</td><td>●</td><td>●</td></tr><tr><td></td><td>openaccessSponsorName</td><td>●</td><td>●</td><td>●</td></tr><tr><td></td><td>openaccessUserLicense</td><td>●</td><td>●</td><td>●</td></tr><tr><td></td><td>oaAllowsAuthorPaid</td><td>●</td><td>●</td><td>●</td></tr><tr><td></td><td>prism:url</td><td>●</td><td>●</td><td>●</td></tr><tr><td></td><td>dc:title</td><td>●</td><td>●</td><td>●</td></tr><tr><td></td><td>prism:issn</td><td>●</td><td>●</td><td>●</td></tr><tr><td></td><td>prism:elssn</td><td>●</td><td>●</td><td>●</td></tr><tr><td></td><td>dc:publisher</td><td>●</td><td>●</td><td>●</td></tr><tr><td></td><td>message</td><td>●</td><td></td><td></td></tr><tr><td></td><td>link ref=scopus-source</td><td>●</td><td>●</td><td>●</td></tr><tr><td></td><td>link ref=homepage</td><td>●</td><td>●</td><td>●</td></tr><tr><td></td><td>prism:aggregationType</td><td></td><td>•</td><td>•</td></tr><tr><td></td><td>subject-area</td><td></td><td>•</td><td>•</td></tr><tr><td>SJRList</td><td>SJR</td><td></td><td>•</td><td>•</td></tr><tr><td>SNIPList</td><td>SNIP</td><td></td><td>•</td><td>•</td></tr><tr><td rowspan="5">citeScoreYearInfoList</td><td>citeScoreCurrentMetric</td><td></td><td>•</td><td>•</td></tr><tr><td>citeScoreCurrentMetricYear</td><td></td><td>•</td><td colspan="1">•</td></tr><tr><td>citeScoreTracker</td><td></td><td>•</td><td colspan="1">•</td></tr><tr><td>citeScoreTrackerYear</td><td></td><td>•</td><td colspan="1">•</td></tr><tr><td>citeScoreYearInfo</td><td></td><td>•</td><td colspan="1">•</td></tr><tr><td></td><td>link ref=coverimage</td><td></td><td>•</td><td>•</td></tr><tr><td rowspan="5">yearly-data/info</td><td>publicationCount</td><td></td><td></td><td>•</td></tr><tr><td>citeCountSCE</td><td></td><td></td><td colspan="1">•</td></tr><tr><td>zeroCitesSCE</td><td></td><td></td><td colspan="1">•</td></tr><tr><td>zeroCitesPercentSCE</td><td></td><td></td><td colspan="1">•</td></tr><tr><td>revPercent</td><td></td><td></td><td colspan="1">•</td></tr></table>

# 8.2. API-specific query parameter options

<table><tr><td>Query parameter</td><td>Options</td><td>Description</td></tr><tr><td rowspan="4">httpAccess</td><td>application/json</td><td>Sets mime type to JSON output; allows multiple records</td></tr><tr><td>application/xml</td><td>Sets mime type to XLM output; allows multiple records</td></tr><tr><td>text/xml</td><td>Sets mime type to XLM as text; allows multiple records</td></tr><tr><td>Image.gif</td><td>Sets mime type to image; only for interface to request a single serial title identified by ISSN.</td></tr></table>

# 9. Subject Classifications API

Depending on the interface used, the Subject Classifications API retrieves the subject classifications associated with content in either ScienceDirect or Scopus. The response is returned as either JSON or XML. Each entry is returned in full with the fields code, abbrev, detail, and description. The query parameter field allows defining which fields should be included in a response.

See page 19 for an example of a request.

# 9.1. Interfaces

Two interfaces are used to submit requests to the Subject Classifications API:

<table><tr><td>URL</td><td>Method</td><td>Description</td></tr><tr><td>https://api/elsevier.com/contentsubject/scidir</td><td>GET</td><td>Returns subject classifications of ScienceDirect content.</td></tr><tr><td>https://api/elsevier.com/contentsubject/scopus</td><td>GET</td><td>Returns subject classifications of Scopus content.</td></tr></table>

# 9.2. API-specific query parameter options

<table><tr><td>Query parameter</td><td>Options</td><td>Description</td></tr><tr><td rowspan="3">httpAccess</td><td>application/json</td><td>Sets mime type to JSON output; allows multiple records</td></tr><tr><td>application/xml</td><td>Sets mime type to XLM output; allows multiple records</td></tr><tr><td>text/xml</td><td>Sets mime type to XLM as text; allows multiple records</td></tr></table>

# 10. Affiliation Retrieval API

Use the Affiliation Retrieval API to request one or more Scopus affiliation profiles using unique Affiliation Identifiers or Electronic Identifiers. Each entry may include links to Scopus Search and to author profiles. Affiliation profiles are indexed and can be searched using the Affiliation Search API.

See page 21 for an example of a request.

# 10.1. Interfaces and views

Use the interface for the relevant identifier to submit requests to the Affiliation Retrieval API:

<table><tr><td>URL</td><td>Method</td><td>Description</td></tr><tr><td>https://api/elsevier.com/content/affiliation/affiliation_id/{affiliation_id}</td><td>GET</td><td>Returns a Scopus affiliation profile based on an Affiliation Identifier.</td></tr><tr><td>https://api/elsevier.com/content/ affiliation/eid/{eid}</td><td>GET</td><td>Returns a Scopus affiliation profile based on an Electronic Identifier.</td></tr></table>

A textual metadata response is returned in one of five views based on access and entitlements: BASIC, LIGHT, STANDARD, DOCUMENTS, or AUTHORS. The default view is LIGHT.

<table><tr><td>Parent field</td><td>Fields included</td><td>BASIC</td><td>LIGHT</td><td>STANDARD</td><td>DOCUMENTS</td><td>AUTHORS</td></tr><tr><td></td><td>link ref=scopus-affiliation</td><td>•</td><td>•</td><td>•</td><td></td><td></td></tr><tr><td></td><td>link ref= self</td><td>•</td><td>•</td><td>•</td><td></td><td></td></tr><tr><td></td><td>prism:url</td><td>•</td><td>•</td><td>•</td><td></td><td></td></tr><tr><td></td><td>dc:identifier</td><td>•</td><td>•</td><td>•</td><td></td><td></td></tr><tr><td></td><td>eid</td><td>•</td><td>•</td><td>•</td><td></td><td></td></tr><tr><td></td><td>link ref=search</td><td></td><td>•</td><td>•</td><td></td><td></td></tr><tr><td></td><td>affiliation-name</td><td></td><td>•</td><td>•</td><td></td><td></td></tr><tr><td></td><td>name-variant</td><td></td><td>•</td><td>•</td><td></td><td></td></tr><tr><td></td><td>address</td><td></td><td>•</td><td>•</td><td></td><td></td></tr><tr><td></td><td>city</td><td></td><td>•</td><td>•</td><td></td><td></td></tr><tr><td></td><td>country</td><td></td><td>•</td><td>•</td><td></td><td></td></tr><tr><td></td><td>author-count</td><td></td><td>•</td><td>•</td><td></td><td>•</td></tr><tr><td></td><td>document-count</td><td></td><td>•</td><td>•</td><td></td><td>•</td></tr><tr><td></td><td>institution-profile</td><td></td><td></td><td>•</td><td></td><td>•</td></tr><tr><td colspan="7">In the DOCUMENTS view, abstracts returned with an affiliation profile include the following fields:</td></tr><tr><td></td><td>prism:url</td><td></td><td></td><td></td><td>•</td><td></td></tr><tr><td></td><td>dc:title</td><td></td><td></td><td></td><td>•</td><td></td></tr><tr><td></td><td>prism:aggregationType</td><td></td><td></td><td></td><td>•</td><td></td></tr><tr><td></td><td>prism:publicationName</td><td></td><td></td><td></td><td>•</td><td></td></tr><tr><td></td><td>prism:issn</td><td></td><td></td><td></td><td>•</td><td></td></tr><tr><td></td><td>prism:volume</td><td></td><td></td><td></td><td>•</td><td></td></tr><tr><td></td><td>prism:issueldentifier</td><td></td><td></td><td></td><td>•</td><td></td></tr><tr><td></td><td>prism:pageRange</td><td></td><td></td><td></td><td>•</td><td></td></tr><tr><td></td><td>prism:coverDate</td><td></td><td></td><td></td><td>•</td><td></td></tr><tr><td></td><td>prism:coverDisplayDate</td><td></td><td></td><td></td><td>•</td><td></td></tr><tr><td></td><td>dc:identifier</td><td></td><td></td><td></td><td>•</td><td></td></tr><tr><td></td><td>eid</td><td></td><td></td><td></td><td>•</td><td></td></tr><tr><td></td><td>prism:doi</td><td></td><td></td><td></td><td>•</td><td></td></tr><tr><td></td><td>dc:creator</td><td></td><td></td><td></td><td>•</td><td></td></tr><tr><td>affiliation</td><td>affilname</td><td></td><td></td><td></td><td>•</td><td></td></tr><tr><td rowspan="2">affiliation</td><td>afid</td><td></td><td></td><td></td><td>•</td><td></td></tr><tr><td>affiliationurl</td><td></td><td></td><td></td><td>•</td><td colspan="1"></td></tr><tr><td rowspan="9">author</td><td>authseq</td><td></td><td></td><td></td><td>•</td><td></td></tr><tr><td>author-uri</td><td></td><td></td><td></td><td>•</td><td colspan="1"></td></tr><tr><td>authid</td><td></td><td></td><td></td><td>•</td><td colspan="1"></td></tr><tr><td>authname</td><td></td><td></td><td></td><td>•</td><td colspan="1"></td></tr><tr><td>orcid</td><td></td><td></td><td></td><td>•</td><td colspan="1"></td></tr><tr><td>given-name</td><td></td><td></td><td></td><td>•</td><td colspan="1"></td></tr><tr><td>surname</td><td></td><td></td><td></td><td>•</td><td colspan="1"></td></tr><tr><td>initials</td><td></td><td></td><td></td><td>•</td><td colspan="1"></td></tr><tr><td>afid</td><td></td><td></td><td></td><td>•</td><td colspan="1"></td></tr><tr><td></td><td>link ref= self</td><td></td><td></td><td></td><td>•</td><td></td></tr><tr><td></td><td>link ref= scopus</td><td></td><td></td><td></td><td>•</td><td></td></tr><tr><td></td><td>link ref= scopus-citedby</td><td></td><td></td><td></td><td>•</td><td></td></tr><tr><td colspan="7">In the AUTHORS view, each author returned with an affiliation profile includes the following fields:</td></tr><tr><td></td><td>dc:identifier</td><td></td><td></td><td></td><td></td><td>•</td></tr><tr><td></td><td>eid</td><td></td><td></td><td></td><td></td><td>•</td></tr><tr><td rowspan="3">preferred-name</td><td>surname</td><td></td><td></td><td></td><td></td><td>•</td></tr><tr><td>given-name</td><td></td><td></td><td></td><td></td><td colspan="1">•</td></tr><tr><td>initials</td><td></td><td></td><td></td><td></td><td colspan="1">•</td></tr><tr><td></td><td>name-variant</td><td></td><td></td><td></td><td></td><td>•</td></tr><tr><td rowspan="5">affiliation-current</td><td>affiliation-name</td><td></td><td></td><td></td><td></td><td>•</td></tr><tr><td>affiliation-city</td><td></td><td></td><td></td><td></td><td colspan="1">•</td></tr><tr><td>affiliation-country</td><td></td><td></td><td></td><td></td><td colspan="1">•</td></tr><tr><td>affiliation-uri</td><td></td><td></td><td></td><td></td><td colspan="1">•</td></tr><tr><td>affiliation-id</td><td></td><td></td><td></td><td></td><td colspan="1">•</td></tr><tr><td rowspan="3">affiliation-history</td><td>affiliation-name</td><td></td><td></td><td></td><td></td><td>•</td></tr><tr><td>affiliation-uri</td><td></td><td></td><td></td><td></td><td colspan="1">•</td></tr><tr><td>affiliation-id</td><td></td><td></td><td></td><td></td><td colspan="1">•</td></tr></table>

# 10.2. API-specific query parameter options

<table><tr><td>Query parameter</td><td>Options</td><td>Description</td></tr><tr><td rowspan="4">httpAccess</td><td>application/json</td><td>Sets mime type to JSON output; allows multiple records</td></tr><tr><td>application/xml</td><td>Sets mime type to XLM output; allows multiple records</td></tr><tr><td>application/rdf+xml</td><td>Sets mime type to RDF/XLM output; allows multiple records</td></tr><tr><td>text/xml</td><td>Sets mime type to XLM as text; allows multiple records</td></tr></table>

Note that the query parameter field is not available for requests in the DOCUMENTS and AUTHORS views.

# 11. Author Retrieval API

Use the Author Retrieval API to request one or more Scopus author profiles using unique identifiers. Each entry may include links to Scopus Search and to affiliation profiles. Author profiles are indexed and can be searched using the Author Search API.

See page 20 for an example of a request.

# 11.1. Interfaces and views

Use the interface for the relevant identifier to submit requests to the Author Retrieval API:

<table><tr><td>URL</td><td>Method</td><td>Description</td></tr><tr><td>https://api/elsevier.com/content/author</td><td>GET</td><td>Returns a Scopus author profile based on an Author or Electronic Identifier.</td></tr><tr><td>https://api/elsevier.com/content/author/author_id/{author_id}</td><td>GET</td><td>Returns a Scopus author profile based on an Author Identifier.</td></tr><tr><td>https://api/elsevier.com/content/author/eid/{eid}</td><td>GET</td><td>Returns a Scopus author profile based on an Electronic Identifier.</td></tr><tr><td>https://api/elsevier.com/content/author/orcid/{orcid}</td><td>GET</td><td>Returns a Scopus author profile based on an Open Researcher and Contributor ID (ORCID).</td></tr></table>

A textual metadata response is returned in one of five views based on access and entitlements: BASIC, METRICS, LIGHT, STANDARD, ENHANCED, or DOCUMENTS. The default view is LIGHT. The DOCUMENTS view is not available in the non-specific author interface.

<table><tr><td>Parent field</td><td>Fields included</td><td>BASIC</td><td>METRICS</td><td>LIGHT</td><td>STANDARD</td><td>ENHANCED</td><td>DOCUMENTS</td></tr><tr><td></td><td>dc:identifier</td><td>•</td><td>•</td><td>•</td><td>•</td><td>•</td><td>•</td></tr><tr><td></td><td>eid</td><td>•</td><td></td><td>•</td><td>•</td><td>•</td><td>•</td></tr><tr><td></td><td>orchid</td><td>•</td><td></td><td>•</td><td>•</td><td>•</td><td>•</td></tr><tr><td></td><td>link ref=scopus-author</td><td>•</td><td></td><td>•</td><td>•</td><td>•</td><td>•</td></tr><tr><td></td><td>link ref= self</td><td>•</td><td></td><td>•</td><td>•</td><td>•</td><td>•</td></tr><tr><td></td><td>prism:url</td><td>•</td><td>•</td><td>•</td><td>•</td><td>•</td><td>•</td></tr><tr><td></td><td>link ref=search</td><td></td><td></td><td>•</td><td>•</td><td>•</td><td>•</td></tr><tr><td></td><td>document-count</td><td></td><td>•</td><td>•</td><td>•</td><td>•</td><td>•</td></tr><tr><td></td><td>cited-by-count</td><td></td><td>•</td><td>•</td><td>•</td><td>•</td><td>•</td></tr><tr><td></td><td>citations-count</td><td></td><td>•</td><td>•</td><td>•</td><td>•</td><td>•</td></tr><tr><td rowspan="3">preferred-name</td><td>surname</td><td></td><td></td><td>•</td><td>•</td><td>•</td><td>•</td></tr><tr><td>given-name</td><td></td><td></td><td>•</td><td>•</td><td>•</td><td colspan="1">•</td></tr><tr><td>initials</td><td></td><td></td><td>•</td><td>•</td><td>•</td><td colspan="1">•</td></tr><tr><td>name-variants</td><td>name-variant</td><td></td><td></td><td>•</td><td>•</td><td>•</td><td>•</td></tr><tr><td rowspan="5">affiliation-current</td><td>affiliation-name</td><td></td><td></td><td>•</td><td>•</td><td>•</td><td>•</td></tr><tr><td>affiliation-city</td><td></td><td></td><td>•</td><td>•</td><td>•</td><td colspan="1">•</td></tr><tr><td>affiliation-country</td><td></td><td></td><td>•</td><td>•</td><td>•</td><td colspan="1">•</td></tr><tr><td>affiliation-uri</td><td></td><td></td><td></td><td>•</td><td>•</td><td colspan="1">•</td></tr><tr><td>affiliation-id</td><td></td><td></td><td></td><td>•</td><td>•</td><td colspan="1">•</td></tr><tr><td rowspan="3">affiliation-history</td><td>affiliation-name</td><td></td><td></td><td></td><td>•</td><td>•</td><td>•</td></tr><tr><td>affiliation-uri</td><td></td><td></td><td></td><td>•</td><td>•</td><td colspan="1">•</td></tr><tr><td>affiliation-id</td><td></td><td></td><td></td><td>•</td><td>•</td><td colspan="1">•</td></tr><tr><td></td><td>author-profile</td><td></td><td></td><td></td><td>•</td><td>•</td><td>•</td></tr><tr><td></td><td>h-index</td><td></td><td>•</td><td></td><td></td><td>•</td><td>•</td></tr><tr><td></td><td>coauthor-count</td><td></td><td>•</td><td></td><td></td><td>•</td><td>•</td></tr><tr><td colspan="8">In the DOCUMENTS view, abstracts returned with an author profile include the following fields:</td></tr><tr><td></td><td>dc:title</td><td></td><td></td><td></td><td></td><td></td><td>•</td></tr><tr><td></td><td>prism:aggregationType</td><td></td><td></td><td></td><td></td><td></td><td>•</td></tr><tr><td></td><td>prism:publicationName</td><td></td><td></td><td></td><td></td><td></td><td>•</td></tr><tr><td></td><td>prism:issn</td><td></td><td></td><td></td><td></td><td></td><td>•</td></tr><tr><td></td><td>prism:volume</td><td></td><td></td><td></td><td></td><td></td><td>•</td></tr><tr><td></td><td>prism:issueldentifier</td><td></td><td></td><td></td><td></td><td></td><td>•</td></tr><tr><td></td><td>prism:pageRange</td><td></td><td></td><td></td><td></td><td></td><td>•</td></tr><tr><td></td><td>prism:coverDate</td><td></td><td></td><td></td><td></td><td></td><td>•</td></tr><tr><td></td><td>prism:coverDisplayDate</td><td></td><td></td><td></td><td></td><td></td><td>•</td></tr><tr><td></td><td>dc:identifier</td><td></td><td></td><td></td><td></td><td></td><td>•</td></tr><tr><td></td><td>eid</td><td></td><td></td><td></td><td></td><td></td><td>•</td></tr><tr><td></td><td>prism:doi</td><td></td><td></td><td></td><td></td><td></td><td>•</td></tr><tr><td></td><td>dc:creator</td><td></td><td></td><td></td><td></td><td></td><td>•</td></tr><tr><td>affiliation</td><td>affilname</td><td></td><td></td><td></td><td></td><td></td><td>•</td></tr><tr><td>affiliation</td><td>afid</td><td></td><td></td><td></td><td></td><td></td><td>•</td></tr><tr><td></td><td>affiliationurl</td><td></td><td></td><td></td><td></td><td></td><td>•</td></tr><tr><td rowspan="9">author</td><td>authseq</td><td></td><td></td><td></td><td></td><td></td><td>•</td></tr><tr><td>author_url</td><td></td><td></td><td></td><td></td><td></td><td colspan="1">•</td></tr><tr><td>authid</td><td></td><td></td><td></td><td></td><td></td><td colspan="1">•</td></tr><tr><td>authname</td><td></td><td></td><td></td><td></td><td></td><td colspan="1">•</td></tr><tr><td>orcid</td><td></td><td></td><td></td><td></td><td></td><td colspan="1">•</td></tr><tr><td>given-name</td><td></td><td></td><td></td><td></td><td></td><td colspan="1">•</td></tr><tr><td>surname</td><td></td><td></td><td></td><td></td><td></td><td colspan="1">•</td></tr><tr><td>initials</td><td></td><td></td><td></td><td></td><td></td><td colspan="1">•</td></tr><tr><td>afid</td><td></td><td></td><td></td><td></td><td></td><td colspan="1">•</td></tr><tr><td></td><td>prism:url</td><td></td><td></td><td></td><td></td><td></td><td>•</td></tr><tr><td></td><td>link ref= self</td><td></td><td></td><td></td><td></td><td></td><td>•</td></tr><tr><td></td><td>link ref= scopus</td><td></td><td></td><td></td><td></td><td></td><td>•</td></tr><tr><td></td><td>link ref= scopus-citedby</td><td></td><td></td><td></td><td></td><td></td><td>•</td></tr></table>

# 11.2. API-specific query parameter options

Submit the criteria for your search using the query query parameter.

<table><tr><td>Query parameter</td><td>Options</td><td>Description</td></tr><tr><td rowspan="4">httpAccess</td><td>application/json</td><td>Sets mime type to JSON output; allows multiple records</td></tr><tr><td>application/xml</td><td>Sets mime type to XLM output; allows multiple records</td></tr><tr><td>application/rdf+xml</td><td>Sets mime type to RDF/XLM output; allows multiple records</td></tr><tr><td>text/xml</td><td>Sets mime type to XLM as text; allows multiple records</td></tr></table>

Note that the query parameter field is not available for requests in the DOCUMENTS view.

# 12. PlumX Metrics API

All active Scopus subscriptions include access to the PlumX Metrics API for the retrieval of PlumX metrics of Scopus documents and related artifacts. PlumX metrics include social media mentions and other sources that go beyond conventional citation data.

See page 24 for an example of a request.

# 12.1. Interfaces

Submit requests to the PlumX Metrics API via the following interface:

<table><tr><td>URL</td><td>Method</td><td>Description</td></tr><tr><td>https://api/elsevier.com/analytics/plumx/{idType}/\{idValue\}</td><td>GET</td><td>Returns aggregate PlumX metrics counts for documents specified via an identifier.</td></tr></table>

# 12.2. API-specific template and query parameter options

Unlike the other Scopus APIs, the PlumX Metrics API uses two template parameters in a request to (a) indicate the identifier type to be used, and (b) provide the identifier value for the document of interest.

<table><tr><td>Template parameter</td><td>Options</td><td>Description</td></tr><tr><td rowspan="6">idType</td><td>doi</td><td>Use the Digital Object Identifier of a document</td></tr><tr><td>elsevierId</td><td>Use the unique Elsevier Identierier of a document</td></tr><tr><td>elsevierPii</td><td>Use the Publication Item Identifier of a document</td></tr><tr><td>ISBN</td><td>Use an International Standard Book Number</td></tr><tr><td>pmcid</td><td>Use the PubMed Central Identifier of a document</td></tr><tr><td>pmid</td><td>Use the MEDLINE PubMed Identifier of a document</td></tr><tr><td>价值</td><td></td><td>Enter the unique identifier of the document of interest</td></tr><tr><td rowspan="3">httpAccept</td><td>application/json</td><td>Sets mime type to JSON output; allows multiple records</td></tr><tr><td>application/xml</td><td>Sets mime type to XLM output; allows multiple records</td></tr><tr><td>application/rgb+xml</td><td>Sets mime type to RDF/XLM output; allows multiple records</td></tr></table>

# 13. Affiliation Search API

This API allows searching the full Scopus body of affiliation profiles. Each search result will, by definition, include a link to an affiliation profile.

See page 22 for an example of a request.

# 13.1. Interfaces and views

A single interface is used to submit requests to the Affiliation Search API:

<table><tr><td>URL</td><td>Method</td><td>Description</td></tr><tr><td>https://api/elsevier.com/content/search/affiliation</td><td>GET</td><td>Conducts a search of Scopus affiliation profiles.</td></tr></table>

A textual metadata response is returned in the default STANDARD view:

<table><tr><td>Fields included</td><td>STANDARD</td></tr><tr><td>link ref= self</td><td>●</td></tr><tr><td>link ref= scopus-affiliation</td><td>●</td></tr><tr><td>link ref= search</td><td>●</td></tr><tr><td>prism:url</td><td>●</td></tr><tr><td>dc:identifier</td><td>●</td></tr><tr><td>eid</td><td>●</td></tr><tr><td>parent-affiliation-id</td><td>●</td></tr><tr><td>affiliation-name</td><td>●</td></tr><tr><td>name-variant</td><td>●</td></tr><tr><td>city</td><td>●</td></tr><tr><td>country</td><td>●</td></tr><tr><td>document-count</td><td>●</td></tr></table>

# 13.2. API-specific query parameter options

![](images/6ac0bbe5ba1b18f8e150b0ca16104192e2b853c55ae8c24649fd7c6270685945.jpg)

Submit your search criteria using the query query parameter. Visit the following link for search tips: Scopus Affiliation Search Guide

<table><tr><td>Query parameter</td><td>Options</td><td>Description</td></tr><tr><td rowspan="3">httpAccess</td><td>application/json</td><td>Sets mime type to JSON output; allows multiple records</td></tr><tr><td>application/xml</td><td>Sets mime type to XLM output; allows multiple records</td></tr><tr><td>Application/atom+xml</td><td>Sets mime type to ATOM/XLM output; allows multiple records</td></tr><tr><td rowspan="2">facet</td><td>affilcity</td><td>Enables faceted navigation according to city of affiliation</td></tr><tr><td>affilcountry</td><td>Enables faceted navigation according to country of affiliation</td></tr><tr><td rowspan="7">sort</td><td>affiliation-name</td><td>Sort by name of affiliation</td></tr><tr><td>city</td><td>Sort by city of affiliation</td></tr><tr><td>country</td><td>Sort by country of affiliation</td></tr><tr><td>document-count</td><td>Sort by number of documents connected to affiliation</td></tr><tr><td>eid</td><td>Sort by Electronic Identifier</td></tr><tr><td>identifier</td><td>Soft by Affiliation Identifier</td></tr><tr><td>parent-affiliation-id</td><td>Soft by Identifier of parent affiliation</td></tr></table>

# 14. Author Search API

This API allows searching the full Scopus body of author profiles. Each search result will, by definition, include a link to an author profile and may also include links to the author's current affiliation profile.

See page 23 for an example of a request.

# 14.1. Interfaces and views

A single interface is used to submit requests to the Author Search API:

<table><tr><td>URL</td><td>Method</td><td>Description</td></tr><tr><td>https://api/elsevier.com/content/search/author</td><td>GET</td><td>Conducts a search of Scopus author profiles.</td></tr></table>

A textual metadata response is returned in the default STANDARD view:

<table><tr><td>Parent field</td><td>Fields included</td><td>STANDARD</td></tr><tr><td></td><td>link ref= self</td><td>●</td></tr><tr><td></td><td>link ref= scopus-author</td><td>●</td></tr><tr><td></td><td>link ref= scopus-citedby</td><td>●</td></tr><tr><td></td><td>link ref= search</td><td>●</td></tr><tr><td></td><td>prism:url</td><td>●</td></tr><tr><td></td><td>dc:identifier</td><td>●</td></tr><tr><td></td><td>eid</td><td>●</td></tr><tr><td></td><td>orcid</td><td>●</td></tr><tr><td></td><td>document-count</td><td>●</td></tr><tr><td></td><td>subject-area</td><td>●</td></tr><tr><td rowspan="3">preferred-name</td><td>surname</td><td>●</td></tr><tr><td>given-name</td><td>●</td></tr><tr><td>initials</td><td>●</td></tr><tr><td></td><td>name-variant</td><td>●</td></tr><tr><td rowspan="5">affiliation-current</td><td>affiliation-name</td><td>●</td></tr><tr><td>affiliation-city</td><td>●</td></tr><tr><td>affiliation-country</td><td>●</td></tr><tr><td>affiliation-id</td><td>●</td></tr><tr><td>affiliation-url</td><td>●</td></tr></table>

# 14.2. API-specific query parameter options

![](images/831c966346477952f5548608ab81cf878d767a763c7f6d67e84d31719efc0e0f.jpg)

Submit your search criteria using the query query parameter. Visit the following link for search tips: Scopus Author Search Guide

<table><tr><td>Query parameter</td><td>Options</td><td>Description</td></tr><tr><td rowspan="3">httpAccess</td><td>application/json</td><td>Sets mime type to JSON output; allows multiple records</td></tr><tr><td>application/xml</td><td>Sets mime type to XLM output; allows multiple records</td></tr><tr><td>Application/atom+xml</td><td>Sets mime type to ATOM/XLM output; allows multiple records</td></tr><tr><td rowspan="6">facet</td><td>affilcity</td><td>Enables faceted navigation according to city of affiliation</td></tr><tr><td>srctitle</td><td>Enables faceted navigation by source title</td></tr><tr><td>af-id</td><td>Enables faceted navigation based on affiliation identifier</td></tr><tr><td>affilcountry</td><td>Enables faceted navigation according to country of affiliation</td></tr><tr><td>auth-subclus</td><td>Enables faceted navigation based on subject area</td></tr><tr><td>active</td><td>Enables faceted navigation based on status of author profile</td></tr><tr><td rowspan="10">sort</td><td>affiliation-name</td><td>Sort by name of affiliation</td></tr><tr><td>affiliation-city</td><td>Sort by city of affiliation</td></tr><tr><td>affiliation-country</td><td>Sort by country of affiliation</td></tr><tr><td>document-count</td><td>Sort by number of documents connected to author profile</td></tr><tr><td>eid</td><td>Sort by Electronic Identifier</td></tr><tr><td>given-name</td><td>Soft by author name</td></tr><tr><td>initials</td><td>Soft by author initials</td></tr><tr><td>surname</td><td>Sort by author surname</td></tr><tr><td>preffirstsort</td><td>Sort by author preferred first name and initials</td></tr><tr><td>affilsortname</td><td>Sort by author&#x27;s current associated affiliation. The name used to sort may be a rearranged or slightly modified version of the institution&#x27;s name (e.g., an English translation of the name)</td></tr></table>

# 15. Scopus Search API

This API allows searching the full Scopus body of abstracts. Each search result will, by definition, include a link to a Scopus abstract and may also include links to a full-text article.

See page 22 for an example of a request.

# 15.1. Interfaces and views

A single interface is used to submit requests to the Scopus Search API:

<table><tr><td>URL</td><td>Method</td><td>Description</td></tr><tr><td>https://api/elsevier.com/content/search/scopus</td><td>GET</td><td>Conducts a search of Scopus abstracts</td></tr></table>

A textual metadata response is returned in one of two views: STANDARD or COMPLETE. The default is the STANDARD view.

<table><tr><td>Parent field</td><td>Fields included</td><td>STANDARD</td><td>COMPLETE</td></tr><tr><td></td><td>link ref= self</td><td>●</td><td>●</td></tr><tr><td></td><td>link ref= scopus</td><td>●</td><td>●</td></tr><tr><td></td><td>link ref= scopus-citedby</td><td>●</td><td>●</td></tr><tr><td></td><td>prism:url</td><td>●</td><td>●</td></tr><tr><td></td><td>dc:identifier</td><td>●</td><td>●</td></tr><tr><td></td><td>eid</td><td>●</td><td>●</td></tr><tr><td></td><td>dc:title</td><td>●</td><td>●</td></tr><tr><td></td><td>prism:aggregationType</td><td>●</td><td>●</td></tr><tr><td></td><td>subtype</td><td>●</td><td>●</td></tr><tr><td></td><td>subtypeDescription</td><td>●</td><td>●</td></tr><tr><td></td><td>citedby-count</td><td>●</td><td>●</td></tr><tr><td></td><td>prism:publicationName</td><td>●</td><td>●</td></tr><tr><td></td><td>prism:ISBN</td><td>●</td><td>●</td></tr><tr><td></td><td>prism:issn</td><td>●</td><td>●</td></tr><tr><td></td><td>prism:volume</td><td>●</td><td>●</td></tr><tr><td></td><td>prism:issueIdentifier</td><td>●</td><td>●</td></tr><tr><td></td><td>prism:pageRange</td><td>●</td><td>●</td></tr><tr><td></td><td>prism:coverDate</td><td>●</td><td>●</td></tr><tr><td></td><td>prism:coverDisplayDate</td><td>●</td><td>●</td></tr><tr><td></td><td>prism:doi</td><td>•</td><td>•</td></tr><tr><td></td><td>pii</td><td>•</td><td>•</td></tr><tr><td></td><td>pubmed-id</td><td>•</td><td>•</td></tr><tr><td></td><td>orcid</td><td>•</td><td>•</td></tr><tr><td></td><td>dc:creator</td><td>•</td><td>•</td></tr><tr><td>openaccess</td><td>openaccessFlag</td><td>•</td><td>•</td></tr><tr><td rowspan="6">affiliation</td><td>affinname</td><td>•</td><td>•</td></tr><tr><td>affiliation-city</td><td>•</td><td colspan="1">•</td></tr><tr><td>affiliation-country</td><td>•</td><td colspan="1">•</td></tr><tr><td>afid</td><td></td><td colspan="1">•</td></tr><tr><td>affiliation_url</td><td></td><td colspan="1">•</td></tr><tr><td>name-variant</td><td></td><td colspan="1">•</td></tr><tr><td rowspan="8">author</td><td>author_url</td><td></td><td>•</td></tr><tr><td>authid</td><td></td><td colspan="1">•</td></tr><tr><td>orcid</td><td></td><td colspan="1">•</td></tr><tr><td>authname</td><td></td><td colspan="1">•</td></tr><tr><td>given-name</td><td></td><td colspan="1">•</td></tr><tr><td>surname</td><td></td><td colspan="1">•</td></tr><tr><td>initials</td><td></td><td colspan="1">•</td></tr><tr><td>afid</td><td></td><td colspan="1">•</td></tr><tr><td></td><td>dc:description</td><td></td><td>•</td></tr><tr><td></td><td>authkeywords</td><td></td><td>•</td></tr><tr><td></td><td>article-number</td><td></td><td>•</td></tr><tr><td></td><td>fund-acr</td><td></td><td>•</td></tr><tr><td></td><td>fund-no</td><td></td><td>•</td></tr><tr><td></td><td>fund-sponsor</td><td></td><td>•</td></tr></table>

# 15.2. API-specific query parameter options

![](images/9aa598897faa0681ef0091d7bce8401190626c809dadf0f8b570fa1c1c9de638.jpg)

Submit your search criteria using the query query parameter. Visit the following link for search tips: Scopus Search Guide

<table><tr><td>Query parameter</td><td>Options</td><td>Description</td></tr><tr><td rowspan="3">httpAccess</td><td>application/json</td><td>Sets mime type to JSON output; allows multiple records</td></tr><tr><td>application/xml</td><td>Sets mime type to XLM output; allows multiple records</td></tr><tr><td>Application/atom+xml</td><td>Sets mime type to ATOM/XLM output; allows multiple records</td></tr><tr><td rowspan="13">facet</td><td>aucite</td><td>Enables faceted navigation by author citation</td></tr><tr><td>au-id</td><td>Enables faceted navigation by Author Identifier</td></tr><tr><td>af-id</td><td>Enables faceted navigation based on Affiliation Identifier</td></tr><tr><td>authname</td><td>Enables faceted navigation based on Author Identifier and name</td></tr><tr><td>country</td><td>Enables faceted navigation based on affiliation country</td></tr><tr><td>exactsrltitle</td><td>Enables faceted navigation based on source title</td></tr><tr><td>fund-sponsor</td><td>Enables faceted navigation based on funding sponsor</td></tr><tr><td>language</td><td>Enables faceted navigation based on language</td></tr><tr><td>openaccess</td><td>Enables faceted navigation based on open access status</td></tr><tr><td>pubyear</td><td>Enables faceted navigation based on publication year</td></tr><tr><td>restype</td><td>Enables faceted navigation based on internal collection</td></tr><tr><td>subjarea</td><td>Enables faceted navigation based on subject area</td></tr><tr><td>srctype</td><td>Enables faceted navigation based on content category</td></tr><tr><td rowspan="12">sort</td><td>artnum</td><td>Sort by article number</td></tr><tr><td>citedby-count</td><td>Sort by cited-by count</td></tr><tr><td>coverDate</td><td>Sort by source cover date</td></tr><tr><td>creator</td><td>Sort by first author</td></tr><tr><td>orig-load-date</td><td>Sort by date of first accession into Scopus</td></tr><tr><td>pagecount</td><td>Sort by page count</td></tr><tr><td>pagefirst</td><td>Sort by number of first page</td></tr><tr><td>pageRange</td><td>Sort by page range</td></tr><tr><td>publicationName</td><td>Sort by name of publication</td></tr><tr><td>pubyear</td><td>Sort by year of publication</td></tr><tr><td>relevancy</td><td>Sort by relevance ranking</td></tr><tr><td>volume</td><td>Sort by volume of source</td></tr></table>

16. Description of query parameters  

<table><tr><td></td><td>Abstract Retrieval</td><td>Citation Count</td><td>Citation Overview</td><td>Serial Title</td><td>Subject</td><td>Affiliation Retrieval</td><td>Author Retrieval</td><td>PlumX Metrics</td><td>Affiliation Search</td><td>Author Search</td><td>Scopus Search</td><td>Brief description</td></tr><tr><td>abbrev</td><td></td><td></td><td></td><td></td><td>•</td><td></td><td></td><td></td><td></td><td></td><td></td><td>Allows filtering response records based upon any string provided in the abbrev attribute. Case-sensitive match of entire field.</td></tr><tr><td>access_token</td><td>•</td><td>•</td><td>•</td><td>•</td><td></td><td>•</td><td>•</td><td>•</td><td>•</td><td>•</td><td>•</td><td>Contains the OAt bearer access token, where the token represents the end-user session key and implies the request will be executed against user-based entitlements. Overrides the HTTP header Authorization.</td></tr><tr><td>alias</td><td></td><td></td><td></td><td></td><td></td><td></td><td>•</td><td></td><td></td><td>•</td><td>•</td><td>Enter “false” to override the default behavior of returning superseded author profiles. Enter “true” or leave empty to prioritize superseded author profiles.</td></tr><tr><td>apiKey</td><td>•</td><td>•</td><td>•</td><td>•</td><td></td><td>•</td><td>•</td><td>•</td><td>•</td><td>•</td><td>•</td><td>Contains a unique application developer key to access the resource. Overrides the http header X-ELS-APIKey.</td></tr><tr><td>author_id</td><td></td><td></td><td>•</td><td></td><td></td><td></td><td>•</td><td></td><td></td><td></td><td></td><td>Pass one or more comma-delimited unique identifiers corresponding to Scopus author profiles. Allows excluding citations for one or more specified authors in responses from the Citation Overview API.</td></tr><tr><td>citation</td><td></td><td></td><td>•</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>Allows excluding citation types; e.g., citation=exclude-self; citation=exclude-books</td></tr><tr><td>co-author</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>•</td><td></td><td>Pass an Identifier to return a list of all associated co-authors. An alternative to the corresponding query criterion.</td></tr><tr><td>code</td><td></td><td></td><td></td><td></td><td>•</td><td></td><td></td><td></td><td></td><td></td><td></td><td>Allows filtering response records based upon any string provided in the code attribute. Case-sensitive match of entire field.</td></tr><tr><td>content</td><td></td><td></td><td></td><td>•</td><td></td><td></td><td></td><td></td><td></td><td></td><td>•</td><td>Indicate one or more source types to be returned in a response. Options for the Serial Title API include “tradejournal”, “journal”, “conferenceproceeding”, “bookseries”. Options for the Scopus Search API include “all”, “core”, and “dummy”.</td></tr><tr><td>count</td><td></td><td></td><td>•</td><td>•</td><td></td><td></td><td></td><td></td><td>•</td><td>•</td><td>•</td><td>Pass the maximum number of records to be returned. If not provided, set to default based on service level.</td></tr><tr><td>cursor</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>•</td><td>To execute deep pagination searching. start is limited to a predefined maximum number of results. Using cursor instead, allows iterating forward sequentially to the end of a result set. Initially accessed by sending a"**" in the first search request. Subsequent requests submit the 'cursor/@next' value from each corresponding response as the 'cursor' value. The 'cursor/@next' value must be URL encoded by the client application. The navigation links ('next') can also be used to navigate to each succeeding search result entry and are URL-encoded by default.</td></tr><tr><td>date</td><td></td><td></td><td>•</td><td>•</td><td></td><td></td><td></td><td></td><td></td><td></td><td>•</td><td>Pass a date range for records to be included in the response. Lowest granularity is year. E.g., date=2005-2007</td></tr><tr><td>description</td><td></td><td></td><td></td><td></td><td>•</td><td></td><td></td><td></td><td></td><td></td><td></td><td>Allows filtering response records based upon any word provided in the primary subject classification description. Case-sensitive match of any portion of the field.</td></tr><tr><td>detail</td><td></td><td></td><td></td><td></td><td>•</td><td></td><td></td><td></td><td></td><td></td><td></td><td>Allows filtering response records based upon any string provided in the detail attribute. Case-sensitive match of any portion of the field.</td></tr><tr><td>doi</td><td></td><td>•</td><td>•</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>Pass the Digital Object Identifier (DOI) of the document of interest. A comma-delimited list of values can be used for textual responses. Only one type of identifier can be used in a request.</td></tr><tr><td>eid</td><td></td><td></td><td></td><td></td><td></td><td></td><td>•</td><td></td><td></td><td></td><td></td><td>Pass one or more comma-delimited unique Electronic IDs corresponding to Scopus author profiles.</td></tr><tr><td>facets</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>•</td><td>•</td><td>•</td><td>Define one or more semicolon-delimited facets to be included in a response. The dimensions of the facet are entered within parentheses. See page 13 for details.</td></tr><tr><td>field</td><td>•</td><td></td><td>•</td><td>•</td><td>•</td><td>•</td><td>•</td><td></td><td>•</td><td>•</td><td>•</td><td>Indicate a comma-delimited list of specific fields to include in the response. Available fields depends on accessible or selected view. Overrides the view parameter.</td></tr><tr><td>httpaccess</td><td>•</td><td>•</td><td>•</td><td>•</td><td>•</td><td>•</td><td>•</td><td>•</td><td>•</td><td>•</td><td>•</td><td>Indicates the format of the response to be generated. Overrides the HTTP Accept. Depending on the API used, options are: imageJPEG, image/gif, application/json, application/xml, text/xml, text/html</td></tr><tr><td>instoken</td><td>•</td><td></td><td></td><td>•</td><td></td><td>•</td><td>•</td><td>•</td><td>•</td><td>•</td><td>•</td><td>Contains an institution token, which in combination with its associated API Key grants access to the resource. Overrides the HTTP header X-ELS-Insttoken.</td></tr><tr><td>issn</td><td></td><td></td><td></td><td>•</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>Pass the international standard serial numbers (ISSN) of one or more serial titles of interest.</td></tr><tr><td>oa</td><td></td><td></td><td></td><td>•</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>Allows filtering records in a response according to Open Access (OA) status. Options include "all" for all source titles, regardless of OA status; "full" to include only sources defined as full OA; "partial" to include only sources defined as partial OA; "none" to include no sources defined as OA (full or partial).</td></tr><tr><td>parentCode</td><td></td><td></td><td></td><td></td><td>•</td><td></td><td></td><td></td><td></td><td></td><td></td><td>Allows filtering response records based upon any string provided in the parentCode attribute. Case-sensitive match of entire field.</td></tr><tr><td>pii</td><td></td><td>•</td><td>•</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>Pass the Publication Item Identifier (PII) of the document of interest. A comma-delimited list of values can be used for textual responses. Only one type of identifier can be used in a request.</td></tr><tr><td>pub</td><td></td><td></td><td></td><td>•</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>Pass a partial or complete publisher name. The API will match a string provided anywhere within the publisher name. Does not accept wildcards.</td></tr><tr><td>pubmed_id</td><td></td><td>•</td><td>•</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>Pass the MEDLINE PubMed Identifier (PMID) of the document of interest. A comma-delimited list of values can be used for textual responses. Only one type of identifier can be used in a request.</td></tr><tr><td>query</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>•</td><td>•</td><td>•</td><td>Pass one or more search criteria. Accepts Boolean operators, proximity operators, wildcards (e.g., *, ?), field codes and subheadings. A required parameter.</td></tr><tr><td>refcount</td><td>•</td><td></td><td></td><td></td><td></td><td>•</td><td>•</td><td></td><td></td><td></td><td></td><td>Pass the maximum number of records to be included in a response. If not provided, set to a default based on service level.</td></tr><tr><td>reqId</td><td>•</td><td>•</td><td>•</td><td>•</td><td></td><td>•</td><td>•</td><td>•</td><td>•</td><td>•</td><td>•</td><td>Contains a client-defined request identifier which is logged in all trace messages of the service. Can be used to track a specific transaction. Overrides the HTTP header X-ELS-ReqId.</td></tr><tr><td>scopus_id</td><td></td><td>•</td><td>•</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>Pass the Scopus Identifier of the document of interest. A comma-delimited list of values can be used for textual responses. Only one type of identifier can be used in a request.</td></tr><tr><td>sort</td><td></td><td></td><td>•</td><td></td><td></td><td></td><td></td><td></td><td>•</td><td>•</td><td>•</td><td>Pass the field name by which results are sorted. Preced with “+” for ascending or “-” for descending. Default is ascending. The Citation Overview API accepts only one field for sorting. In the Search APIs, up to three comma-delimited fields can be specified, their listed order defining the precedence. E.g., sort=+sortname,-certscore</td></tr><tr><td>start</td><td></td><td></td><td>•</td><td>•</td><td></td><td></td><td></td><td></td><td>•</td><td>•</td><td>•</td><td>Pass the record number from which to start downloading records retrieved by a request. Note that numbering starts at 0, which is also the default if not specified.</td></tr><tr><td>startref</td><td>•</td><td></td><td></td><td></td><td></td><td>•</td><td>•</td><td></td><td></td><td></td><td></td><td>Pass the numeric value of the starting position for records in a response (e.g., startref=5). Note that numbering starts at 0, which is also the default if not specified.</td></tr><tr><td>subj</td><td></td><td></td><td></td><td>•</td><td></td><td></td><td></td><td></td><td></td><td></td><td>•</td><td>Pass a Scopus subject area abbreviation associated with the content category desired (e.g., ARTS – Arts and Humanities, ENER – Energy). Note that subject mapping varies based on the environment in which the request is executed. All Scopus subject classifications can be found here: Subject classifications</td></tr><tr><td>subjCode</td><td></td><td></td><td></td><td>•</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>Pass one or more Scopus subject area codes associated with the content category desired. All Scopus subject classifications and subject area codes can be found here: Subject classifications</td></tr><tr><td>suppressNavLinks</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>•</td><td>•</td><td>•</td><td>Enter “true” to suppress the inclusion of top-level navigation links in the response. The default is “false”.</td></tr><tr><td>title</td><td></td><td></td><td></td><td>•</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>Pass a partial or complete serial title. The API will match a string provided anywhere within the title name. Does not accept wildcards.</td></tr><tr><td>ver</td><td>•</td><td>•</td><td>•</td><td>•</td><td></td><td>•</td><td>•</td><td></td><td>•</td><td>•</td><td>•</td><td>Pass the version of the resource that should be received. Overrides the HTTP header X-ELS-ResourceVersion. In the case of Search APIs, options include: “subjexpand” to add detail to the subject-area field by detailing each entry as a subject (available only in the Author Search API); “facetexpand” to add new fields under each facet returned (where applicable); “allexpand” executes both facetexpand and subjexpand (where applicable); “new” to return the most recent and prototyped features.</td></tr><tr><td>view</td><td>•</td><td></td><td>•</td><td>•</td><td></td><td>•</td><td>•</td><td></td><td>•</td><td>•</td><td>•</td><td>Indicate the view to be used for the response. See each API for a description of corresponding views.</td></tr></table>

# 17. Description of elements associated with Abstracts included in a response

<table><tr><td></td><td>Element</td><td></td><td>Description</td></tr><tr><td></td><td>prism:url</td><td></td><td>URI to content from the Abstract Retrieval API</td></tr><tr><td>1</td><td>identifier</td><td></td><td></td></tr><tr><td></td><td>dc:identifier</td><td>1</td><td>Scopus Document Identifier</td></tr><tr><td></td><td>prism:doi</td><td>1</td><td>Digital Objective Identifier</td></tr><tr><td></td><td>pii</td><td>1</td><td>Publication Item Identifier</td></tr><tr><td></td><td>Scopus_id</td><td>1</td><td>Scopus ID</td></tr><tr><td></td><td>pubmed_id</td><td>1</td><td>MEDLINE PubMed Identifier</td></tr><tr><td></td><td>eid</td><td>1</td><td>Electronic Identifier</td></tr><tr><td></td><td>dc:title</td><td></td><td>Title of document</td></tr><tr><td></td><td>prism:aggregationType</td><td></td><td>Publication type of the source of the document</td></tr><tr><td></td><td>subtype</td><td></td><td>Code for the type of document (e.g., “ar” for article)</td></tr><tr><td></td><td>subtypeDescription</td><td></td><td>Description of the type of document</td></tr><tr><td></td><td>openaccess</td><td></td><td>Indicates the open access status of a document (e.g., “0” for not open, “1” for gold, “2” for green)</td></tr><tr><td></td><td>openaccessFlag</td><td></td><td>A legacy field set to “false” when a document is not open access (openaccess set to “0”), “true” when a document has gold access (openaccess set to “1”), and left empty for other open access status types</td></tr><tr><td></td><td>citedby-count</td><td></td><td>Number of citations of the document</td></tr><tr><td></td><td>citation-count</td><td></td><td>Number of citations in the document</td></tr><tr><td></td><td>prism-publicationName</td><td></td><td>Name of the publication containing the document</td></tr><tr><td></td><td>prism:ISBN</td><td></td><td>International Standard Book Number of the publication containing the document</td></tr><tr><td></td><td>prism:issn</td><td></td><td>International Standard Serial Number of the publication containing the document</td></tr><tr><td></td><td>prism:volume</td><td></td><td>Volume of the publication containing the document</td></tr><tr><td></td><td>prism:issueldentifier</td><td></td><td>Issue of the publication containing the document</td></tr><tr><td></td><td>prism:pageRange</td><td></td><td>Contains the start and end page of a document (e.g., 17-43)</td></tr><tr><td></td><td>prism:coverDate</td><td></td><td>Date of publication (YYYY-MM-DD)</td></tr><tr><td></td><td>prism:coverDisplayDate</td><td></td><td>Publication date of original text</td></tr><tr><td></td><td>article-number</td><td></td><td>Article number of the document</td></tr><tr><td></td><td>Authkeywords</td><td></td><td>Author keywords</td></tr><tr><td></td><td>fund-acr</td><td></td><td>Acronym of funding agency</td></tr><tr><td></td><td>fund-no</td><td></td><td>Identifier of funding agency</td></tr><tr><td></td><td>fund-sponsor</td><td></td><td>Name of funding agency</td></tr><tr><td>2</td><td>dc:creator</td><td></td><td>First author on the document</td></tr><tr><td></td><td>auid</td><td>2</td><td>Scopus Author Identifier for the first author</td></tr><tr><td></td><td>author_url</td><td>2</td><td>URI to content from Author Retrieval API for the author</td></tr><tr><td>3</td><td>affiliation</td><td></td><td></td></tr><tr><td></td><td>affiliation-name</td><td>3</td><td>Name of affiliation of the first author</td></tr><tr><td></td><td>affiliation-city</td><td>3</td><td>City of affiliation of first author</td></tr><tr><td></td><td>affiliation-country</td><td>3</td><td>Country of affiliation of first author</td></tr><tr><td></td><td>afid</td><td>3</td><td>Affiliation Identifier</td></tr><tr><td></td><td>affiliationurl</td><td>3</td><td>URI to content from the Affiliation Retrieval API</td></tr><tr><td></td><td>name-variant</td><td>3</td><td>Alternatiate affiliation names</td></tr><tr><td>4</td><td>authors</td><td></td><td>Information on the other authors of the document</td></tr><tr><td>5</td><td>author</td><td>4</td><td>Bucket for each of the other authors</td></tr><tr><td></td><td>authname</td><td>5</td><td>Concatenated fields surname and initials (e.g., Nowak K.J.)</td></tr><tr><td></td><td>given-name</td><td>5</td><td>First name of author</td></tr><tr><td></td><td>surname</td><td>5</td><td>Last name of author</td></tr><tr><td></td><td>Initials</td><td>5</td><td>Initials of author</td></tr><tr><td></td><td>authid</td><td>5</td><td>Author Identifier</td></tr><tr><td></td><td>auid</td><td>5</td><td>Author Identifier</td></tr><tr><td></td><td>author-uri</td><td>5</td><td>URI to content from Author Retrieval API for the author</td></tr><tr><td></td><td>affiliation</td><td>5</td><td>Name of affiliation of the author</td></tr><tr><td></td><td>afid</td><td>5</td><td>Affiliation Identifier</td></tr><tr><td></td><td>affiliation-uri</td><td>5</td><td>URI to content from the Affiliation Retrieval API</td></tr><tr><td></td><td>orcid</td><td>5</td><td>Open Researcher and Contributor Identifier</td></tr><tr><td></td><td>dc:description</td><td></td><td>Abstract text</td></tr><tr><td></td><td>intid</td><td></td><td>Institution ID</td></tr><tr><td>6</td><td>subject-areas</td><td></td><td></td></tr><tr><td></td><td>subject-area</td><td>6</td><td>Each subject area relevant to the document</td></tr><tr><td></td><td>code</td><td>6</td><td>Code for each subject area relevant to the document</td></tr><tr><td></td><td>abbrev</td><td>6</td><td>Abbreviation for each subject area relevant to the document</td></tr><tr><td></td><td>item</td><td></td><td>Includes the original text of the abstract, including:
• Code for the language of the original document using the label /abstract-retrieval-response/item/bibrecord/head/citation-info/citation-language/@xml:lang
• Author keywords using /abstract-retrieval-response/item/bibrecord/head/citation-info/author-keywords/author-keyword
• Index keywords (not available by default) using /abstract-retrieval-response/item/bibrecord/head/enhancement/descriptor/group/descriptors/descriptor/mainterm</td></tr><tr><td></td><td>link ref=self</td><td></td><td>URI to content from the Abstract Retrieval API</td></tr><tr><td></td><td>link ref=scopus</td><td></td><td>URL to the details of a Scopus Abstract; does not require md5 encryption</td></tr><tr><td></td><td>link ref=scopus-citedby</td><td></td><td>URL to document cited-by content in Scopus</td></tr><tr><td></td><td>h-index</td><td></td><td>The h-index of the documents returned</td></tr><tr><td></td><td>citeinfo</td><td></td><td>Information about a citing document</td></tr><tr><td></td><td>dc:identifier</td><td></td><td>Scopus Document Identifier of the citing document</td></tr><tr><td></td><td>prism:url</td><td></td><td>URI to content from the Abstract Retrieval API about the citing document</td></tr><tr><td></td><td>Dc:title</td><td></td><td>Title of the citing document</td></tr><tr><td>7</td><td>author</td><td></td><td>Information for each author on a citing document</td></tr><tr><td></td><td>initials</td><td>7</td><td>Author's initials</td></tr><tr><td></td><td>index-name</td><td>7</td><td>Author's name</td></tr><tr><td></td><td>surname</td><td>7</td><td>Author's surname</td></tr><tr><td></td><td>authid</td><td>7</td><td>Author Identifier</td></tr><tr><td></td><td>author-uri</td><td>7</td><td>URI to content from Author Retrieval API for the author</td></tr><tr><td></td><td>sort-year</td><td></td><td>Year for sorting documents</td></tr><tr><td></td><td>prism:publicationName</td><td></td><td>Name of the publication containing the document (e.g., journal, book, etc)</td></tr><tr><td></td><td>prism:volume</td><td></td><td>Volume of the publication</td></tr><tr><td></td><td>prism:issueldentifier</td><td></td><td>Number of the issue containing the document</td></tr><tr><td></td><td>prism:startingPage</td><td></td><td>Starting page of the document</td></tr><tr><td></td><td>prism:endingPage</td><td></td><td>Ending page of the document</td></tr><tr><td></td><td>prism:issn</td><td></td><td>International Standard Serial Number of the publication</td></tr><tr><td></td><td>citationType</td><td></td><td>Type of citation (e.g., article)</td></tr><tr><td></td><td>pcc</td><td></td><td>Previous column count</td></tr><tr><td></td><td>cc</td><td></td><td>Column count</td></tr><tr><td></td><td>Icc</td><td></td><td>Later column count</td></tr><tr><td></td><td>rangeCount</td><td></td><td>Sum of all cc fields</td></tr><tr><td></td><td>citeCountHeader</td><td></td><td></td></tr><tr><td></td><td>rowTotal</td><td></td><td>Sum of pcc, Icc, rangeCount fields</td></tr><tr><td></td><td>prevColumnHeader</td><td></td><td>Column Heading for citation counts before the passed in range</td></tr><tr><td></td><td>columnHeading</td><td></td><td>Column Heading (ie., 2013)</td></tr><tr><td></td><td>laterColumnHeading</td><td></td><td>Column Heading for citation counts after the passed in range</td></tr><tr><td></td><td>prevColumnTotal</td><td></td><td>Column Total for citation counts before the passed in range</td></tr><tr><td></td><td>columnTotal</td><td></td><td>Column Total</td></tr><tr><td></td><td>laterColumnTotal</td><td></td><td>Column Heading for citation counts after the passed in range</td></tr><tr><td></td><td>rangeColumnTotal</td><td></td><td>Sum of all columnTotal fields</td></tr><tr><td></td><td>grandTotal</td><td></td><td>Sum of prevColumnTotal, laterColumnTotal, and rangeColumnTotal</td></tr><tr><td></td><td>Serial Title</td><td></td><td></td></tr><tr><td></td><td>openaccess</td><td></td><td>Open Access status (1/0)</td></tr><tr><td></td><td>openaccessArticle</td><td></td><td>Open Access status (true/false)</td></tr><tr><td></td><td>openArchiveArticle</td><td></td><td>Open Archive status (true/false)</td></tr><tr><td></td><td>openaccessType</td><td></td><td>Open Access status (Full/Partial)</td></tr><tr><td></td><td>openaccessStartDate</td><td></td><td>Date when open access became available</td></tr><tr><td></td><td>openaccessSponsorName</td><td></td><td>Open Access metadata</td></tr><tr><td></td><td>openaccessSponsorType</td><td></td><td>Open Access metadata</td></tr><tr><td></td><td>openaccessUserLicense</td><td></td><td>Open Access metadata</td></tr><tr><td></td><td>oaAllowsAuthorPaid</td><td></td><td>Open Access metadata</td></tr><tr><td></td><td>prism:url</td><td></td><td>URL w/ ISSN</td></tr><tr><td></td><td>dc:title</td><td></td><td>Title of the search result</td></tr><tr><td></td><td>prism:issn</td><td></td><td>ISSN</td></tr><tr><td></td><td>prism:elsen</td><td></td><td>Electronic ISSN</td></tr><tr><td></td><td>dc:publisher</td><td></td><td>Publisher</td></tr><tr><td></td><td>message</td><td></td><td>A message that says that a full list of Scopus titles can be found on info.scopus.sciverse.com</td></tr><tr><td></td><td>link ref=scopus-source</td><td></td><td>URL of the Scopus source page (format http://www.scopus.com/source/sourceInfo.url?sourceid=[SOURCEID])</td></tr><tr><td></td><td>link ref=homepage</td><td></td><td>Third-party journal homepage URL (i.e., the URL of the journal homepage button that Scopus points to from OHUB)</td></tr><tr><td></td><td>prism:aggregationType</td><td></td><td>Serial type</td></tr><tr><td></td><td>subject-area</td><td></td><td>Subject area (Scopus classification), using label, and on the same level of granularity as the subject classification on the Scopus source page</td></tr><tr><td>8</td><td>citeScoreYearInfoList</td><td></td><td>Cite Score information</td></tr><tr><td></td><td>citeScoreCurrentMetric</td><td>8</td><td>Indicates the calculation/value for the latest complete year. Four years in total.</td></tr><tr><td></td><td>citeScoreCurrentMetricYear</td><td>8</td><td>Indicates the year of the citation score in the field citeScoreCurrentMetric; i.e., the latest complete year. Four years in total.</td></tr><tr><td></td><td>citeScoreTracker</td><td>8</td><td>Indicates the calculation/value for the in-progress year and is subject to change every month throughout the year. Four years in total. For example, citeScoreTracker 2023 updates every month until it reaches its annual value in May 2024. That value then becomes the annual citation score value for 2023 provided in field siteScoreCurrentMetric, and a new citeScoreTracker begins for 2024.</td></tr><tr><td></td><td>citeScoreTrackerYear</td><td>8</td><td>Indicates the year of the citation score in the field citeScoreTracker; i.e., the latest in-progress year. Four years in total.</td></tr><tr><td></td><td>citeScoreYearInfo</td><td>8</td><td>Note that the list of citeScoreYearInfo details only appear when retrieving individual sources (i.e., by issn, ISBN, or source id) and will not appear for general searches that return multiple entries</td></tr><tr><td></td><td>link ref=coverimage</td><td></td><td>URL of cover image (format http://api.elsevier.com/content/serial/issn:[ISSN]?view=coverimage)</td></tr><tr><td>9</td><td>yearly-data/info</td><td></td><td>Historical data</td></tr><tr><td></td><td>publicationCount</td><td>9</td><td>Number of documents by year</td></tr><tr><td></td><td>citeCountSCE</td><td>9</td><td>Number of cited documents</td></tr><tr><td></td><td>zeroCitesSCE</td><td>9</td><td>Percentage of not-cited documents</td></tr><tr><td></td><td>revPercent</td><td>9</td><td>Percentage of review article documents</td></tr><tr><td>10</td><td>SJRList</td><td></td><td></td></tr><tr><td></td><td>SJR</td><td>10</td><td>Scientific Journal Ranking</td></tr><tr><td>11</td><td>SNIPList</td><td></td><td></td></tr><tr><td></td><td>SNIP</td><td>11</td><td>Source Normalized Impact per Paper</td></tr></table>

# 18. Description of elements associated with Author included in a response

<table><tr><td></td><td>Element</td><td></td><td>Description</td></tr><tr><td></td><td>dc:identifier</td><td></td><td>Scopus Author Identifier</td></tr><tr><td></td><td>eid</td><td></td><td>Electronic Identifier</td></tr><tr><td></td><td>orchid</td><td></td><td>Open Researcher and Contributor Identifier</td></tr><tr><td></td><td>link ref=scopus-author</td><td></td><td>URL to the details page of a Scopus author profile; not enabled for preview</td></tr><tr><td></td><td>link ref=scopus-citedby</td><td></td><td>URL to Author cited-by content in Scopus</td></tr><tr><td></td><td>link ref= self</td><td></td><td>URI to content from the Author Retrieval API</td></tr><tr><td></td><td>prism:url</td><td></td><td>URI to content from the Author Retrieval API</td></tr><tr><td></td><td>link ref=search</td><td></td><td>URL to content on the abstracts associated with the author retrieved with the Socrates Search API (i.e., a Scopus document search by Author ID). Request URL: http://api.elsevier.com/content/search/scopus?query=authid({authid})</td></tr><tr><td></td><td>document-count</td><td></td><td>Number of documents authored</td></tr><tr><td></td><td>cited-by-count</td><td></td><td>Number of citing documents</td></tr><tr><td></td><td>citations-count</td><td></td><td>Number of citations</td></tr><tr><td></td><td>subject-area</td><td></td><td>Subject areas associated with author (maximum of three)</td></tr><tr><td>1</td><td>preferred-name</td><td></td><td></td></tr><tr><td></td><td>surname</td><td>1</td><td>Preferred author last name</td></tr><tr><td></td><td>given-name</td><td>1</td><td>Preferred author first name</td></tr><tr><td></td><td>initials</td><td>1</td><td>Author initials</td></tr><tr><td>2</td><td>name-variants</td><td></td><td></td></tr><tr><td></td><td>name-variant</td><td>2</td><td>Variants of the author's name (may be restricted to a maximum of three In some APIs)</td></tr><tr><td>3</td><td>affiliation-current</td><td></td><td></td></tr><tr><td></td><td>affiliation-name</td><td>3</td><td>Name of current affiliation</td></tr><tr><td></td><td>affiliation-city</td><td>3</td><td>City of current affiliation</td></tr><tr><td></td><td>affiliation-country</td><td>3</td><td>Country of current affiliation</td></tr><tr><td></td><td>affiliation-uri</td><td>3</td><td>URI to content from the Affiliation Retrieval API</td></tr><tr><td></td><td>affiliation-id</td><td>3</td><td>Affiliation Identifier for current affiliation</td></tr><tr><td>4</td><td>affiliation-history</td><td></td><td></td></tr><tr><td></td><td>affiliation-name</td><td>4</td><td>Name of historical affiliation</td></tr><tr><td></td><td>affiliation-uri</td><td>4</td><td>URI to content from Affiliation Retrieval API for historical affiliation</td></tr><tr><td></td><td>affiliation-id</td><td>4</td><td>Identifier of historical affiliation</td></tr><tr><td></td><td>author-profile</td><td></td><td>Original text of Author Profile</td></tr><tr><td></td><td>h-index</td><td></td><td>h-index of the author</td></tr><tr><td></td><td>coauthor-count</td><td></td><td>Number of co-authors associated with the author</td></tr></table>

# 19. Description of elements associated with Affiliation included in a response

<table><tr><td></td><td>Element</td><td></td><td>Description</td></tr><tr><td></td><td>link ref=scopus-affiliation</td><td></td><td>URL to the Scopus affiliation profile; not enabled for preview</td></tr><tr><td></td><td>link ref=self</td><td></td><td>URI to content from the Affiliation Retrieval API</td></tr><tr><td></td><td>prism:url</td><td></td><td>URI to content from the Affiliation Retrieval API</td></tr><tr><td></td><td>dc:identifier</td><td></td><td>Affiliation Identifier</td></tr><tr><td></td><td>eid</td><td></td><td>Electronic Identifier</td></tr><tr><td></td><td>link ref=search</td><td></td><td>URL to content on the abstracts associated with the affiliation retrieved with the Scopus Search API (i.e., a Scopus document search by Affiliation ID). Request URL: http://api.elsevier.com/content/search/scopus?query=afid({afid})</td></tr><tr><td></td><td>affiliation-name</td><td></td><td>Name of affiliation</td></tr><tr><td></td><td>name-variant</td><td></td><td>Variants of the affiliation name</td></tr><tr><td></td><td>address</td><td></td><td>Street address of affiliation</td></tr><tr><td></td><td>city</td><td></td><td>City of affiliation</td></tr><tr><td></td><td>country</td><td></td><td>Country of affiliation</td></tr><tr><td></td><td>author-count</td><td></td><td>Number of authors associated with affiliation</td></tr><tr><td></td><td>document-count</td><td></td><td>Number of documents associated with affiliation</td></tr><tr><td></td><td>institution-profile</td><td></td><td>Original text of affiliation profile</td></tr><tr><td></td><td>Parent-affiliation-id</td><td></td><td>Affiliation Identifier of parent affiliation</td></tr></table>