





<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
  <link rel="dns-prefetch" href="https://assets-cdn.github.com">
  <link rel="dns-prefetch" href="https://avatars0.githubusercontent.com">
  <link rel="dns-prefetch" href="https://avatars1.githubusercontent.com">
  <link rel="dns-prefetch" href="https://avatars2.githubusercontent.com">
  <link rel="dns-prefetch" href="https://avatars3.githubusercontent.com">
  <link rel="dns-prefetch" href="https://github-cloud.s3.amazonaws.com">
  <link rel="dns-prefetch" href="https://user-images.githubusercontent.com/">



  <link crossorigin="anonymous" media="all" integrity="sha512-FCg44VGg5ax/5MpZ8otwiPE+/tG1/Sq67mKkl6agbqgoScZtJyXhQSFQMIJfOHMZZ+yXDINb8nEiws60SiLohg==" rel="stylesheet" href="https://assets-cdn.github.com/assets/frameworks-5aa6d9885579bb2359f66266aee26f3b.css" />
  <link crossorigin="anonymous" media="all" integrity="sha512-+/hqp+gOyKak+oOrmncIDqvw8rgk69e9HtwA/O+2PG25IJgS6L+sciem4Dqu4L77m8UaEYWxYhXeRhxzzaDk3Q==" rel="stylesheet" href="https://assets-cdn.github.com/assets/github-2bf9c5ab90af2104656120603fa7ae6a.css" />
  
  
  <link crossorigin="anonymous" media="all" integrity="sha512-E5+zFFBnEQXXps9ieNpzSUgN31FS1ZOYDzZM5E3r76jqHW8BhrYO8haxfx+cWTmvHb3aMzOHd33+lpo9LKEGMw==" rel="stylesheet" href="https://assets-cdn.github.com/assets/site-6ad63d41698318191bd9870787a0a634.css" />
  

  <meta name="viewport" content="width=device-width">
  
  <title>how-to-read-code/how-to-read-code.md at master · aredridel/how-to-read-code · GitHub</title>
    <meta name="description" content="A talk about how to read source code. Contribute to aredridel/how-to-read-code development by creating an account on GitHub.">
    <link rel="search" type="application/opensearchdescription+xml" href="/opensearch.xml" title="GitHub">
  <link rel="fluid-icon" href="https://github.com/fluidicon.png" title="GitHub">
  <meta property="fb:app_id" content="1401488693436528">

    
    <meta property="og:image" content="https://avatars1.githubusercontent.com/u/2876?s=400&amp;v=4" /><meta property="og:site_name" content="GitHub" /><meta property="og:type" content="object" /><meta property="og:title" content="aredridel/how-to-read-code" /><meta property="og:url" content="https://github.com/aredridel/how-to-read-code" /><meta property="og:description" content="A talk about how to read source code. Contribute to aredridel/how-to-read-code development by creating an account on GitHub." />

  <link rel="assets" href="https://assets-cdn.github.com/">
  
  <meta name="pjax-timeout" content="1000">
  
  <meta name="request-id" content="9A54:20C9:A37182:DB135F:5BC1CC5E" data-pjax-transient>


  

  <meta name="selected-link" value="repo_source" data-pjax-transient>

      <meta name="google-site-verification" content="KT5gs8h0wvaagLKAVWq8bbeNwnZZK1r1XQysX3xurLU">
    <meta name="google-site-verification" content="ZzhVyEFwb7w3e0-uOTltm8Jsck2F5StVihD0exw2fsA">
    <meta name="google-site-verification" content="GXs5KoUUkNCoaAZn7wPN-t01Pywp9M3sEjnt_3_ZWPc">

  <meta name="octolytics-host" content="collector.githubapp.com" /><meta name="octolytics-app-id" content="github" /><meta name="octolytics-event-url" content="https://collector.githubapp.com/github-external/browser_event" /><meta name="octolytics-dimension-request_id" content="9A54:20C9:A37182:DB135F:5BC1CC5E" /><meta name="octolytics-dimension-region_edge" content="iad" /><meta name="octolytics-dimension-region_render" content="iad" />
<meta name="analytics-location" content="/&lt;user-name&gt;/&lt;repo-name&gt;/blob/show" data-pjax-transient="true" />



    <meta name="google-analytics" content="UA-3769691-2">


<meta class="js-ga-set" name="dimension1" content="Logged Out">



  

      <meta name="hostname" content="github.com">
    <meta name="user-login" content="">

      <meta name="expected-hostname" content="github.com">
    <meta name="js-proxy-site-detection-payload" content="MWQ4MWI2NmU3ZjdkMGViZTc3ZGNiODI0YWQzMGFkZGFlNzU1YTk2MWQwMGVkMDI3NTRjZTRlZTU0YjBiYmVmNnx7InJlbW90ZV9hZGRyZXNzIjoiMTE0LjI0OC42OS4xNjAiLCJyZXF1ZXN0X2lkIjoiOUE1NDoyMEM5OkEzNzE4MjpEQjEzNUY6NUJDMUNDNUUiLCJ0aW1lc3RhbXAiOjE1Mzk0Mjc0MjQsImhvc3QiOiJnaXRodWIuY29tIn0=">

    <meta name="enabled-features" content="DASHBOARD_V2_LAYOUT_OPT_IN,EXPLORE_DISCOVER_REPOSITORIES,UNIVERSE_BANNER,MARKETPLACE_PLAN_RESTRICTION_EDITOR,ISSUE_AND_PR_HOVERCARDS">

  <meta name="html-safe-nonce" content="ade476c385fd8295754f5d5b9e5f847ed2b9a832">

  <meta http-equiv="x-pjax-version" content="2445a9d8f1e3921e095f7142cee041b8">
  

      <link href="https://github.com/aredridel/how-to-read-code/commits/master.atom" rel="alternate" title="Recent Commits to how-to-read-code:master" type="application/atom+xml">

  <meta name="go-import" content="github.com/aredridel/how-to-read-code git https://github.com/aredridel/how-to-read-code.git">

  <meta name="octolytics-dimension-user_id" content="2876" /><meta name="octolytics-dimension-user_login" content="aredridel" /><meta name="octolytics-dimension-repository_id" content="31600256" /><meta name="octolytics-dimension-repository_nwo" content="aredridel/how-to-read-code" /><meta name="octolytics-dimension-repository_public" content="true" /><meta name="octolytics-dimension-repository_is_fork" content="false" /><meta name="octolytics-dimension-repository_network_root_id" content="31600256" /><meta name="octolytics-dimension-repository_network_root_nwo" content="aredridel/how-to-read-code" /><meta name="octolytics-dimension-repository_explore_github_marketplace_ci_cta_shown" content="false" />


    <link rel="canonical" href="https://github.com/aredridel/how-to-read-code/blob/master/how-to-read-code.md" data-pjax-transient>


  <meta name="browser-stats-url" content="https://api.github.com/_private/browser/stats">

  <meta name="browser-errors-url" content="https://api.github.com/_private/browser/errors">

  <link rel="mask-icon" href="https://assets-cdn.github.com/pinned-octocat.svg" color="#000000">
  <link rel="icon" type="image/x-icon" class="js-site-favicon" href="https://assets-cdn.github.com/favicon.ico">

<meta name="theme-color" content="#1e2327">



  <link rel="manifest" href="/manifest.json" crossOrigin="use-credentials">

  </head>

  <body class="logged-out env-production page-blob">
    

  <div class="position-relative js-header-wrapper ">
    <a href="#start-of-content" tabindex="1" class="px-2 py-4 bg-blue text-white show-on-focus js-skip-to-content">Skip to content</a>
    <div id="js-pjax-loader-bar" class="pjax-loader-bar"><div class="progress"></div></div>

    
    
    



        
<header class="Header header-logged-out  position-relative f4 py-3" role="banner">
  <div class="container-lg d-flex px-3">
    <div class="d-flex flex-justify-between flex-items-center">
      <a class="header-logo-invertocat my-0" href="https://github.com/" aria-label="Homepage" data-ga-click="(Logged out) Header, go to homepage, icon:logo-wordmark">
        <svg height="32" class="octicon octicon-mark-github" viewBox="0 0 16 16" version="1.1" width="32" aria-hidden="true"><path fill-rule="evenodd" d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0 0 16 8c0-4.42-3.58-8-8-8z"/></svg>
      </a>

    </div>

    <div class="HeaderMenu d-flex flex-justify-between flex-auto">
        <nav class="mt-0">
          <ul class="d-flex list-style-none">
              <li class="ml-2">
                <a class="js-selected-navigation-item HeaderNavlink px-0 py-2 m-0" data-ga-click="Header, click, Nav menu - item:features" data-selected-links="/features /features/project-management /features/code-review /features/project-management /features/integrations /features" href="/features">
                  Features
</a>              </li>
              <li class="ml-4">
                <a class="js-selected-navigation-item HeaderNavlink px-0 py-2 m-0" data-ga-click="Header, click, Nav menu - item:business" data-selected-links="/business /business/security /business/customers /business" href="/business">
                  Business
</a>              </li>

              <li class="ml-4">
                <a class="js-selected-navigation-item HeaderNavlink px-0 py-2 m-0" data-ga-click="Header, click, Nav menu - item:explore" data-selected-links="/explore /trending /trending/developers /integrations /integrations/feature/code /integrations/feature/collaborate /integrations/feature/ship showcases showcases_search showcases_landing /explore" href="/explore">
                  Explore
</a>              </li>

              <li class="ml-4">
                    <a class="js-selected-navigation-item HeaderNavlink px-0 py-2 m-0" data-ga-click="Header, click, Nav menu - item:marketplace" data-selected-links=" /marketplace" href="/marketplace">
                      Marketplace
</a>              </li>
              <li class="ml-4">
                <a class="js-selected-navigation-item HeaderNavlink px-0 py-2 m-0" data-ga-click="Header, click, Nav menu - item:pricing" data-selected-links="/pricing /pricing/developer /pricing/team /pricing/business-hosted /pricing/business-enterprise /pricing" href="/pricing">
                  Pricing
</a>              </li>
          </ul>
        </nav>

      <div class="d-flex">
          <div class="d-lg-flex flex-items-center mr-3">
            <div class="header-search scoped-search site-scoped-search js-site-search position-relative js-jump-to"
  role="combobox"
  aria-owns="jump-to-results"
  aria-label="Search or jump to"
  aria-haspopup="listbox"
  aria-expanded="false"
>
  <div class="position-relative">
    <!-- '"` --><!-- </textarea></xmp> --></option></form><form class="js-site-search-form" data-scope-type="Repository" data-scope-id="31600256" data-scoped-search-url="/aredridel/how-to-read-code/search" data-unscoped-search-url="/search" action="/aredridel/how-to-read-code/search" accept-charset="UTF-8" method="get"><input name="utf8" type="hidden" value="&#x2713;" />
      <label class="form-control header-search-wrapper header-search-wrapper-jump-to position-relative d-flex flex-justify-between flex-items-center js-chromeless-input-container">
        <input type="text"
          class="form-control header-search-input jump-to-field js-jump-to-field js-site-search-focus js-site-search-field is-clearable"
          data-hotkey="s,/"
          name="q"
          value=""
          placeholder="Search"
          data-unscoped-placeholder="Search GitHub"
          data-scoped-placeholder="Search"
          autocapitalize="off"
          aria-autocomplete="list"
          aria-controls="jump-to-results"
          data-jump-to-suggestions-path="/_graphql/GetSuggestedNavigationDestinations#csrf-token=yoB25ly3C32vv4VK6tb4DUXkLXoJ4S+z5HsiSqwDTFvjtljirVsW+DoaR5HLv1jCPbqvIpbodJFLZWOfnPD/Ng=="
          spellcheck="false"
          autocomplete="off"
          >
          <input type="hidden" class="js-site-search-type-field" name="type" >
            <img src="https://assets-cdn.github.com/images/search-shortcut-hint.svg" alt="" class="mr-2 header-search-key-slash">

            <div class="Box position-absolute overflow-hidden d-none jump-to-suggestions js-jump-to-suggestions-container">
              <ul class="d-none js-jump-to-suggestions-template-container">
                <li class="d-flex flex-justify-start flex-items-center p-0 f5 navigation-item js-navigation-item" role="option">
                  <a tabindex="-1" class="no-underline d-flex flex-auto flex-items-center p-2 jump-to-suggestions-path js-jump-to-suggestion-path js-navigation-open" href="">
                    <div class="jump-to-octicon js-jump-to-octicon flex-shrink-0 mr-2 text-center d-none">
                      <svg height="16" width="16" class="octicon octicon-repo flex-shrink-0 js-jump-to-octicon-repo d-none" title="Repository" aria-label="Repository" viewBox="0 0 12 16" version="1.1" role="img"><path fill-rule="evenodd" d="M4 9H3V8h1v1zm0-3H3v1h1V6zm0-2H3v1h1V4zm0-2H3v1h1V2zm8-1v12c0 .55-.45 1-1 1H6v2l-1.5-1.5L3 16v-2H1c-.55 0-1-.45-1-1V1c0-.55.45-1 1-1h10c.55 0 1 .45 1 1zm-1 10H1v2h2v-1h3v1h5v-2zm0-10H2v9h9V1z"/></svg>
                      <svg height="16" width="16" class="octicon octicon-project flex-shrink-0 js-jump-to-octicon-project d-none" title="Project" aria-label="Project" viewBox="0 0 15 16" version="1.1" role="img"><path fill-rule="evenodd" d="M10 12h3V2h-3v10zm-4-2h3V2H6v8zm-4 4h3V2H2v12zm-1 1h13V1H1v14zM14 0H1a1 1 0 0 0-1 1v14a1 1 0 0 0 1 1h13a1 1 0 0 0 1-1V1a1 1 0 0 0-1-1z"/></svg>
                      <svg height="16" width="16" class="octicon octicon-search flex-shrink-0 js-jump-to-octicon-search d-none" title="Search" aria-label="Search" viewBox="0 0 16 16" version="1.1" role="img"><path fill-rule="evenodd" d="M15.7 13.3l-3.81-3.83A5.93 5.93 0 0 0 13 6c0-3.31-2.69-6-6-6S1 2.69 1 6s2.69 6 6 6c1.3 0 2.48-.41 3.47-1.11l3.83 3.81c.19.2.45.3.7.3.25 0 .52-.09.7-.3a.996.996 0 0 0 0-1.41v.01zM7 10.7c-2.59 0-4.7-2.11-4.7-4.7 0-2.59 2.11-4.7 4.7-4.7 2.59 0 4.7 2.11 4.7 4.7 0 2.59-2.11 4.7-4.7 4.7z"/></svg>
                    </div>

                    <img class="avatar mr-2 flex-shrink-0 js-jump-to-suggestion-avatar d-none" alt="" aria-label="Team" src="" width="28" height="28">

                    <div class="jump-to-suggestion-name js-jump-to-suggestion-name flex-auto overflow-hidden text-left no-wrap css-truncate css-truncate-target">
                    </div>

                    <div class="border rounded-1 flex-shrink-0 bg-gray px-1 text-gray-light ml-1 f6 d-none js-jump-to-badge-search">
                      <span class="js-jump-to-badge-search-text-default d-none" aria-label="in this repository">
                        In this repository
                      </span>
                      <span class="js-jump-to-badge-search-text-global d-none" aria-label="in all of GitHub">
                        All GitHub
                      </span>
                      <span aria-hidden="true" class="d-inline-block ml-1 v-align-middle">↵</span>
                    </div>

                    <div aria-hidden="true" class="border rounded-1 flex-shrink-0 bg-gray px-1 text-gray-light ml-1 f6 d-none d-on-nav-focus js-jump-to-badge-jump">
                      Jump to
                      <span class="d-inline-block ml-1 v-align-middle">↵</span>
                    </div>
                  </a>
                </li>
              </ul>
              <ul class="d-none js-jump-to-no-results-template-container">
                <li class="d-flex flex-justify-center flex-items-center p-3 f5 d-none">
                  <span class="text-gray">No suggested jump to results</span>
                </li>
              </ul>

              <ul id="jump-to-results" role="listbox" class="js-navigation-container jump-to-suggestions-results-container js-jump-to-suggestions-results-container" >
                <li class="d-flex flex-justify-center flex-items-center p-0 f5">
                  <img src="https://assets-cdn.github.com/images/spinners/octocat-spinner-128.gif" alt="Octocat Spinner Icon" class="m-2" width="28">
                </li>
              </ul>
            </div>
      </label>
</form>  </div>
</div>

          </div>

        <span class="d-inline-block">
            <div class="HeaderNavlink px-0 py-2 m-0">
              <a class="text-bold text-white no-underline" href="/login?return_to=%2Faredridel%2Fhow-to-read-code%2Fblob%2Fmaster%2Fhow-to-read-code.md" data-ga-click="(Logged out) Header, clicked Sign in, text:sign-in">Sign in</a>
                <span class="text-gray">or</span>
                <a class="text-bold text-white no-underline" href="/join?source=header-repo" data-ga-click="(Logged out) Header, clicked Sign up, text:sign-up">Sign up</a>
            </div>
        </span>
      </div>
    </div>
  </div>
</header>

  </div>

  <div id="start-of-content" class="show-on-focus"></div>

    <div id="js-flash-container">


</div>



  <div role="main" class="application-main ">
        <div itemscope itemtype="http://schema.org/SoftwareSourceCode" class="">
    <div id="js-repo-pjax-container" data-pjax-container >
      







  <div class="pagehead repohead instapaper_ignore readability-menu experiment-repo-nav  ">
    <div class="repohead-details-container clearfix container">

      <ul class="pagehead-actions">
  <li>
      <a href="/login?return_to=%2Faredridel%2Fhow-to-read-code"
    class="btn btn-sm btn-with-count tooltipped tooltipped-s"
    aria-label="You must be signed in to watch a repository" rel="nofollow">
    <svg class="octicon octicon-eye v-align-text-bottom" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M8.06 2C3 2 0 8 0 8s3 6 8.06 6C13 14 16 8 16 8s-3-6-7.94-6zM8 12c-2.2 0-4-1.78-4-4 0-2.2 1.8-4 4-4 2.22 0 4 1.8 4 4 0 2.22-1.78 4-4 4zm2-4c0 1.11-.89 2-2 2-1.11 0-2-.89-2-2 0-1.11.89-2 2-2 1.11 0 2 .89 2 2z"/></svg>
    Watch
  </a>
  <a class="social-count" href="/aredridel/how-to-read-code/watchers"
     aria-label="17 users are watching this repository">
    17
  </a>

  </li>

  <li>
      <a href="/login?return_to=%2Faredridel%2Fhow-to-read-code"
    class="btn btn-sm btn-with-count tooltipped tooltipped-s"
    aria-label="You must be signed in to star a repository" rel="nofollow">
    <svg class="octicon octicon-star v-align-text-bottom" viewBox="0 0 14 16" version="1.1" width="14" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M14 6l-4.9-.64L7 1 4.9 5.36 0 6l3.6 3.26L2.67 14 7 11.67 11.33 14l-.93-4.74L14 6z"/></svg>
    Star
  </a>

    <a class="social-count js-social-count" href="/aredridel/how-to-read-code/stargazers"
      aria-label="307 users starred this repository">
      307
    </a>

  </li>

  <li>
      <a href="/login?return_to=%2Faredridel%2Fhow-to-read-code"
        class="btn btn-sm btn-with-count tooltipped tooltipped-s"
        aria-label="You must be signed in to fork a repository" rel="nofollow">
        <svg class="octicon octicon-repo-forked v-align-text-bottom" viewBox="0 0 10 16" version="1.1" width="10" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M8 1a1.993 1.993 0 0 0-1 3.72V6L5 8 3 6V4.72A1.993 1.993 0 0 0 2 1a1.993 1.993 0 0 0-1 3.72V6.5l3 3v1.78A1.993 1.993 0 0 0 5 15a1.993 1.993 0 0 0 1-3.72V9.5l3-3V4.72A1.993 1.993 0 0 0 8 1zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zm3 10c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zm3-10c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"/></svg>
        Fork
      </a>

    <a href="/aredridel/how-to-read-code/network/members" class="social-count"
       aria-label="38 users forked this repository">
      38
    </a>
  </li>
</ul>

      <h1 class="public ">
  <svg class="octicon octicon-repo" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9H3V8h1v1zm0-3H3v1h1V6zm0-2H3v1h1V4zm0-2H3v1h1V2zm8-1v12c0 .55-.45 1-1 1H6v2l-1.5-1.5L3 16v-2H1c-.55 0-1-.45-1-1V1c0-.55.45-1 1-1h10c.55 0 1 .45 1 1zm-1 10H1v2h2v-1h3v1h5v-2zm0-10H2v9h9V1z"/></svg>
  <span class="author" itemprop="author"><a class="url fn" rel="author" href="/aredridel">aredridel</a></span><!--
--><span class="path-divider">/</span><!--
--><strong itemprop="name"><a data-pjax="#js-repo-pjax-container" href="/aredridel/how-to-read-code">how-to-read-code</a></strong>

</h1>

    </div>
    
<nav class="reponav js-repo-nav js-sidenav-container-pjax container"
     itemscope
     itemtype="http://schema.org/BreadcrumbList"
     role="navigation"
     data-pjax="#js-repo-pjax-container">

  <span itemscope itemtype="http://schema.org/ListItem" itemprop="itemListElement">
    <a class="js-selected-navigation-item selected reponav-item" itemprop="url" data-hotkey="g c" data-selected-links="repo_source repo_downloads repo_commits repo_releases repo_tags repo_branches repo_packages /aredridel/how-to-read-code" href="/aredridel/how-to-read-code">
      <svg class="octicon octicon-code" viewBox="0 0 14 16" version="1.1" width="14" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M9.5 3L8 4.5 11.5 8 8 11.5 9.5 13 14 8 9.5 3zm-5 0L0 8l4.5 5L6 11.5 2.5 8 6 4.5 4.5 3z"/></svg>
      <span itemprop="name">Code</span>
      <meta itemprop="position" content="1">
</a>  </span>

    <span itemscope itemtype="http://schema.org/ListItem" itemprop="itemListElement">
      <a itemprop="url" data-hotkey="g i" class="js-selected-navigation-item reponav-item" data-selected-links="repo_issues repo_labels repo_milestones /aredridel/how-to-read-code/issues" href="/aredridel/how-to-read-code/issues">
        <svg class="octicon octicon-issue-opened" viewBox="0 0 14 16" version="1.1" width="14" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"/></svg>
        <span itemprop="name">Issues</span>
        <span class="Counter">0</span>
        <meta itemprop="position" content="2">
</a>    </span>

  <span itemscope itemtype="http://schema.org/ListItem" itemprop="itemListElement">
    <a data-hotkey="g p" itemprop="url" class="js-selected-navigation-item reponav-item" data-selected-links="repo_pulls checks /aredridel/how-to-read-code/pulls" href="/aredridel/how-to-read-code/pulls">
      <svg class="octicon octicon-git-pull-request" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M11 11.28V5c-.03-.78-.34-1.47-.94-2.06C9.46 2.35 8.78 2.03 8 2H7V0L4 3l3 3V4h1c.27.02.48.11.69.31.21.2.3.42.31.69v6.28A1.993 1.993 0 0 0 10 15a1.993 1.993 0 0 0 1-3.72zm-1 2.92c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zM4 3c0-1.11-.89-2-2-2a1.993 1.993 0 0 0-1 3.72v6.56A1.993 1.993 0 0 0 2 15a1.993 1.993 0 0 0 1-3.72V4.72c.59-.34 1-.98 1-1.72zm-.8 10c0 .66-.55 1.2-1.2 1.2-.65 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"/></svg>
      <span itemprop="name">Pull requests</span>
      <span class="Counter">0</span>
      <meta itemprop="position" content="3">
</a>  </span>


    <a data-hotkey="g b" class="js-selected-navigation-item reponav-item" data-selected-links="repo_projects new_repo_project repo_project /aredridel/how-to-read-code/projects" href="/aredridel/how-to-read-code/projects">
      <svg class="octicon octicon-project" viewBox="0 0 15 16" version="1.1" width="15" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M10 12h3V2h-3v10zm-4-2h3V2H6v8zm-4 4h3V2H2v12zm-1 1h13V1H1v14zM14 0H1a1 1 0 0 0-1 1v14a1 1 0 0 0 1 1h13a1 1 0 0 0 1-1V1a1 1 0 0 0-1-1z"/></svg>
      Projects
      <span class="Counter" >0</span>
</a>


  <a class="js-selected-navigation-item reponav-item" data-selected-links="repo_graphs repo_contributors dependency_graph pulse alerts /aredridel/how-to-read-code/pulse" href="/aredridel/how-to-read-code/pulse">
    <svg class="octicon octicon-graph" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M16 14v1H0V0h1v14h15zM5 13H3V8h2v5zm4 0H7V3h2v10zm4 0h-2V6h2v7z"/></svg>
    Insights
</a>

</nav>


  </div>

<div class="container new-discussion-timeline experiment-repo-nav  ">
  <div class="repository-content ">

    

  
    <a class="d-none js-permalink-shortcut" data-hotkey="y" href="/aredridel/how-to-read-code/blob/2354e2db75dcf44ce1aded34d6318d98601ff37a/how-to-read-code.md">Permalink</a>

    <!-- blob contrib key: blob_contributors:v21:609cb57ace577859f9e0aefabbc22960 -->

        <div class="signup-prompt-bg rounded-1">
      <div class="signup-prompt p-4 text-center mb-4 rounded-1">
        <div class="position-relative">
          <!-- '"` --><!-- </textarea></xmp> --></option></form><form action="/site/dismiss_signup_prompt" accept-charset="UTF-8" method="post"><input name="utf8" type="hidden" value="&#x2713;" /><input type="hidden" name="authenticity_token" value="NlS2o3uFff/pF4+SJK7HQDFav8TljEo/UyuveMLZSicq+zHzqpTee4/GTO6742tXdXryyARlD1Gp/mn1oU5erQ==" />
            <button type="submit" class="position-absolute top-0 right-0 btn-link link-gray" data-ga-click="(Logged out) Sign up prompt, clicked Dismiss, text:dismiss">
              Dismiss
            </button>
</form>          <h3 class="pt-2">Join GitHub today</h3>
          <p class="col-6 mx-auto">GitHub is home to over 28 million developers working together to host and review code, manage projects, and build software together.</p>
          <a class="btn btn-primary" href="/join?source=prompt-blob-show" data-ga-click="(Logged out) Sign up prompt, clicked Sign up, text:sign-up">Sign up</a>
        </div>
      </div>
    </div>


    <div class="file-navigation">
      
<div class="select-menu branch-select-menu js-menu-container js-select-menu float-left">
  <button class=" btn btn-sm select-menu-button js-menu-target css-truncate" data-hotkey="w"
    
    type="button" aria-label="Switch branches or tags" aria-expanded="false" aria-haspopup="true">
      <i>Branch:</i>
      <span class="js-select-button css-truncate-target">master</span>
  </button>

  <div class="select-menu-modal-holder js-menu-content js-navigation-container" data-pjax>

    <div class="select-menu-modal">
      <div class="select-menu-header">
        <svg class="octicon octicon-x js-menu-close" role="img" aria-label="Close" viewBox="0 0 12 16" version="1.1" width="12" height="16"><path fill-rule="evenodd" d="M7.48 8l3.75 3.75-1.48 1.48L6 9.48l-3.75 3.75-1.48-1.48L4.52 8 .77 4.25l1.48-1.48L6 6.52l3.75-3.75 1.48 1.48L7.48 8z"/></svg>
        <span class="select-menu-title">Switch branches/tags</span>
      </div>

      <div class="select-menu-filters">
        <div class="select-menu-text-filter">
          <input type="text" aria-label="Filter branches/tags" id="context-commitish-filter-field" class="form-control js-filterable-field js-navigation-enable" placeholder="Filter branches/tags">
        </div>
        <div class="select-menu-tabs">
          <ul>
            <li class="select-menu-tab">
              <a href="#" data-tab-filter="branches" data-filter-placeholder="Filter branches/tags" class="js-select-menu-tab" role="tab">Branches</a>
            </li>
            <li class="select-menu-tab">
              <a href="#" data-tab-filter="tags" data-filter-placeholder="Find a tag…" class="js-select-menu-tab" role="tab">Tags</a>
            </li>
          </ul>
        </div>
      </div>

      <div class="select-menu-list select-menu-tab-bucket js-select-menu-tab-bucket" data-tab-filter="branches" role="menu">

        <div data-filterable-for="context-commitish-filter-field" data-filterable-type="substring">


            <a class="select-menu-item js-navigation-item js-navigation-open selected"
               href="/aredridel/how-to-read-code/blob/master/how-to-read-code.md"
               data-name="master"
               data-skip-pjax="true"
               rel="nofollow">
              <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                master
              </span>
            </a>
        </div>

          <div class="select-menu-no-results">Nothing to show</div>
      </div>

      <div class="select-menu-list select-menu-tab-bucket js-select-menu-tab-bucket" data-tab-filter="tags">
        <div data-filterable-for="context-commitish-filter-field" data-filterable-type="substring">


            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/aredridel/how-to-read-code/tree/v1.0.0/how-to-read-code.md"
              data-name="v1.0.0"
              data-skip-pjax="true"
              rel="nofollow">
              <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v1.0.0">
                v1.0.0
              </span>
            </a>
        </div>

        <div class="select-menu-no-results">Nothing to show</div>
      </div>

    </div>
  </div>
</div>

      <div class="BtnGroup float-right">
        <a href="/aredridel/how-to-read-code/find/master"
              class="js-pjax-capture-input btn btn-sm BtnGroup-item"
              data-pjax
              data-hotkey="t">
          Find file
        </a>
        <clipboard-copy for="blob-path" class="btn btn-sm BtnGroup-item">
          Copy path
        </clipboard-copy>
      </div>
      <div id="blob-path" class="breadcrumb">
        <span class="repo-root js-repo-root"><span class="js-path-segment"><a data-pjax="true" href="/aredridel/how-to-read-code"><span>how-to-read-code</span></a></span></span><span class="separator">/</span><strong class="final-path">how-to-read-code.md</strong>
      </div>
    </div>


    
  <div class="commit-tease">
      <span class="float-right">
        <a class="commit-tease-sha" href="/aredridel/how-to-read-code/commit/2354e2db75dcf44ce1aded34d6318d98601ff37a" data-pjax>
          2354e2d
        </a>
        <relative-time datetime="2016-04-07T20:25:01Z">Apr 7, 2016</relative-time>
      </span>
      <div>
        <a rel="author" data-skip-pjax="true" data-hovercard-type="user" data-hovercard-url="/hovercards?user_id=2876" data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="/aredridel"><img class="avatar" src="https://avatars1.githubusercontent.com/u/2876?s=40&amp;v=4" width="20" height="20" alt="@aredridel" /></a>
        <a class="user-mention" rel="author" data-hovercard-type="user" data-hovercard-url="/hovercards?user_id=2876" data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="/aredridel">aredridel</a>
          <a data-pjax="true" title="A few slide separating tweaks" class="message" href="/aredridel/how-to-read-code/commit/2354e2db75dcf44ce1aded34d6318d98601ff37a">A few slide separating tweaks</a>
      </div>

    <div class="commit-tease-contributors">
      
<details class="details-reset details-overlay details-overlay-dark lh-default text-gray-dark float-left mr-2" id="blob_contributors_box">
  <summary class="btn-link" aria-haspopup="dialog"  >
    
    <span><strong>2</strong> contributors</span>
  </summary>
  <details-dialog class="Box Box--overlay d-flex flex-column anim-fade-in fast " aria-label="Users who have contributed to this file">
    <div class="Box-header">
      <button class="Box-btn-octicon btn-octicon float-right" type="button" aria-label="Close dialog" data-close-dialog>
        <svg class="octicon octicon-x" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.48 8l3.75 3.75-1.48 1.48L6 9.48l-3.75 3.75-1.48-1.48L4.52 8 .77 4.25l1.48-1.48L6 6.52l3.75-3.75 1.48 1.48L7.48 8z"/></svg>
      </button>
      <h3 class="Box-title">Users who have contributed to this file</h3>
    </div>
    
        <ul class="list-style-none overflow-auto">
            <li class="Box-row">
              <a class="link-gray-dark no-underline" href="/aredridel">
                <img class="avatar mr-2" alt="" src="https://avatars1.githubusercontent.com/u/2876?s=40&amp;v=4" width="20" height="20" />
                aredridel
</a>            </li>
            <li class="Box-row">
              <a class="link-gray-dark no-underline" href="/stevemao">
                <img class="avatar mr-2" alt="" src="https://avatars3.githubusercontent.com/u/6316590?s=40&amp;v=4" width="20" height="20" />
                stevemao
</a>            </li>
        </ul>

  </details-dialog>
</details>
          <a class="avatar-link" data-hovercard-type="user" data-hovercard-url="/hovercards?user_id=2876" data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="/aredridel/how-to-read-code/commits/master/how-to-read-code.md?author=aredridel">
      <img class="avatar" src="https://avatars1.githubusercontent.com/u/2876?s=40&amp;v=4" width="20" height="20" alt="@aredridel" /> 
</a>    <a class="avatar-link" data-hovercard-type="user" data-hovercard-url="/hovercards?user_id=6316590" data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="/aredridel/how-to-read-code/commits/master/how-to-read-code.md?author=stevemao">
      <img class="avatar" src="https://avatars3.githubusercontent.com/u/6316590?s=40&amp;v=4" width="20" height="20" alt="@stevemao" /> 
</a>

    </div>
  </div>



    <div class="file ">
      <div class="file-header">
  <div class="file-actions">

    <div class="BtnGroup">
      <a id="raw-url" class="btn btn-sm BtnGroup-item" href="/aredridel/how-to-read-code/raw/master/how-to-read-code.md">Raw</a>
        <a class="btn btn-sm js-update-url-with-hash BtnGroup-item" data-hotkey="b" href="/aredridel/how-to-read-code/blame/master/how-to-read-code.md">Blame</a>
      <a rel="nofollow" class="btn btn-sm BtnGroup-item" href="/aredridel/how-to-read-code/commits/master/how-to-read-code.md">History</a>
    </div>


        <button type="button" class="btn-octicon disabled tooltipped tooltipped-nw"
          aria-label="You must be signed in to make or propose changes">
          <svg class="octicon octicon-pencil" viewBox="0 0 14 16" version="1.1" width="14" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M0 12v3h3l8-8-3-3-8 8zm3 2H1v-2h1v1h1v1zm10.3-9.3L12 6 9 3l1.3-1.3a.996.996 0 0 1 1.41 0l1.59 1.59c.39.39.39 1.02 0 1.41z"/></svg>
        </button>
        <button type="button" class="btn-octicon btn-octicon-danger disabled tooltipped tooltipped-nw"
          aria-label="You must be signed in to make or propose changes">
          <svg class="octicon octicon-trashcan" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M11 2H9c0-.55-.45-1-1-1H5c-.55 0-1 .45-1 1H2c-.55 0-1 .45-1 1v1c0 .55.45 1 1 1v9c0 .55.45 1 1 1h7c.55 0 1-.45 1-1V5c.55 0 1-.45 1-1V3c0-.55-.45-1-1-1zm-1 12H3V5h1v8h1V5h1v8h1V5h1v8h1V5h1v9zm1-10H2V3h9v1z"/></svg>
        </button>
  </div>

  <div class="file-info">
      675 lines (455 sloc)
      <span class="file-info-divider"></span>
    19.7 KB
  </div>
</div>

      
  <div id="readme" class="readme blob instapaper_body">
    <article class="markdown-body entry-content" itemprop="text"><h1><a id="user-content-how-to-read-source-code" class="anchor" aria-hidden="true" href="#how-to-read-source-code"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>How To Read Source Code</h1>
<p>Aria Stewart</p>
<p>@aredridel</p>
<p>^ I work on the krakenjs team at PayPal. I work on internationalization and localization.</p>
<p>^ More specifically, what I do is wrangle the increasingly complicated ways that strings are concatenated in our web apps.</p>
<p>^ So why do we concatenate strings in complicated ways instead of simple ones?</p>
<p>^ Different responsibilities. I'll come back to this later.</p>
<hr>
<p>I almost didn't give this talk.</p>
<p>^ Like there's any programmers out there who don't read source code.</p>
<p>^ Then I met a bunch of programmers who don't read source code. And I talked to some more who wouldn't read anything but the examples. And I met a <em>lot</em> of beginning programmers who have a hard time figuring out where to start.</p>
<p>^ When they were maintaining software, they'd do almost anything to avoid reading the source code.</p>
<hr>
<h2><a id="user-content-what-do-we-mean-when-we-say-reading-source-code" class="anchor" aria-hidden="true" href="#what-do-we-mean-when-we-say-reading-source-code"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>What do we mean when we say "reading source code"?</h2>
<p>Reading for comprehension</p>
<p>... to find bugs</p>
<p>... to find interactions</p>
<p>... to review</p>
<p>... to see the interface</p>
<p>... to learn!</p>
<hr>
<h2><a id="user-content-reading-isnt-linear" class="anchor" aria-hidden="true" href="#reading-isnt-linear"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>Reading isn't linear</h2>
<p>^ We think we can read source code like a book. Crack the introduction or README, then read through from chapter one to chapter two, on toward the conclusion.</p>
<p>^ It's not like that. For a great many programs, we can't even prove that they end.</p>
<p>^ We skip back and forth from chapter to chapter, module to module. We can read the module straight through but we won't have the definitions of things from other modules. We can read in execution order, but we won't know where we're going more than one call site down.</p>
<hr>
<h2><a id="user-content-reading-order" class="anchor" aria-hidden="true" href="#reading-order"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>Reading Order</h2>
<p>Do you start at the entry point of a package?</p>
<p>How about in a browser?</p>
<p>Maybe find the biggest source code file and read that first.</p>
<p>Try setting a breakpoint early and tracing down through functions in a debugger.</p>
<p>Try setting a breakpoint deep in the code, and reading each function in the call stack.</p>
<hr>
<p>Kinds of source code</p>
<ul>
<li>Javascript</li>
<li>C++</li>
<li>ES6</li>
<li>Coffee Script</li>
<li>Shell Script</li>
</ul>
<p>^ Who reads any of these kinds of source code?</p>
<hr>
<ul>
<li>SNOBOL</li>
<li>APL</li>
<li>Befunge</li>
<li>Forth</li>
<li>Perl</li>
<li>Other people's javascript</li>
</ul>
<p>^ How about these?</p>
<hr>
<p>Another way to think of kinds of source code</p>
<ul>
<li>Glue</li>
<li>Interface-defining</li>
<li>Implementation</li>
<li>Algorithmic</li>
<li>Configuring</li>
<li>Tasking</li>
</ul>
<p>^ There's a lot of study of algorithmic source code out there because that's what academia produces: algorithms, the little, often mathematical ways of doing things. All the others are a lot more nebulous but I think a lot more interesting. They're certainly the bulk of what most people write when they're programming computers.</p>
<p>^ Of course, sometimes, something does more than one of these things. Many times, in fact. Figuring out what it's trying to be can be one of the first tasks.</p>
<hr>
<h2><a id="user-content-whats-glue" class="anchor" aria-hidden="true" href="#whats-glue"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>What's 'Glue'?</h2>
<p>^ Not all the interfaces we want to use play nice together. Glue is the plumbing connecting things together. Middleware, promises vs callbacks binding code, inflating arguments into objects or breaking objects apart. All that's glue.</p>
<hr>
<h2><a id="user-content-how-do-you-read-glue" class="anchor" aria-hidden="true" href="#how-do-you-read-glue"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>How do you read glue?</h2>
<p>^ We're looking for how two interfaces are shaped differently, and what's common between them.</p>
<hr>
<p>This is from Ben Drucker's <code>stream-to-promise</code></p>
<div class="highlight highlight-source-js"><pre><span class="pl-smi">internals</span>.<span class="pl-en">writable</span> <span class="pl-k">=</span> <span class="pl-k">function</span> (<span class="pl-smi">stream</span>) {
  <span class="pl-k">return</span> <span class="pl-k">new</span> <span class="pl-en">Promise</span>(<span class="pl-k">function</span> (<span class="pl-smi">resolve</span>, <span class="pl-smi">reject</span>) {
    <span class="pl-smi">stream</span>.<span class="pl-en">once</span>(<span class="pl-s"><span class="pl-pds">'</span>finish<span class="pl-pds">'</span></span>, resolve);
    <span class="pl-smi">stream</span>.<span class="pl-en">once</span>(<span class="pl-s"><span class="pl-pds">'</span>error<span class="pl-pds">'</span></span>, reject);
  });
};</pre></div>
<p>^ The two interfaces we're talking about here are node streams and promises.</p>
<p>^ The things they have in common are that they do work until they finish, in node with an event, in promises by calling the resolution functions.</p>
<p>^ Now the thing you can notice while you're reading is that promises really can only be resolved once, but streams can actually emit the same event multiple times. They don't usually, but as programmers we usually know the difference between can't and shouldn't.</p>
<hr>
<p>More glue!</p>
<div class="highlight highlight-source-js"><pre><span class="pl-k">var</span> record <span class="pl-k">=</span> {
    name<span class="pl-k">:</span> (<span class="pl-smi">input</span>.<span class="pl-c1">name</span> <span class="pl-k">||</span> <span class="pl-s"><span class="pl-pds">'</span><span class="pl-pds">'</span></span>).<span class="pl-en">trim</span>(),
    age<span class="pl-k">:</span> <span class="pl-c1">isNaN</span>(<span class="pl-c1">Number</span>(<span class="pl-smi">input</span>.<span class="pl-smi">age</span>)) <span class="pl-k">?</span> <span class="pl-c1">null</span> <span class="pl-k">:</span> <span class="pl-c1">Number</span>(<span class="pl-smi">input</span>.<span class="pl-smi">age</span>),
    email<span class="pl-k">:</span> <span class="pl-en">validateEmail</span>(<span class="pl-smi">input</span>.<span class="pl-smi">email</span>.<span class="pl-en">trim</span>())
}</pre></div>
<p>^ More things to think about in glue: How are errors handled?</p>
<p>^ It's worth asking if any of these things throw? Do they delete bad values? Maybe they coerce them into being okay-enough values? Are these the right choices for the context they're operating in? Are conversions lossy?</p>
<hr>
<h2><a id="user-content-whats-interface-defining-code" class="anchor" aria-hidden="true" href="#whats-interface-defining-code"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>What's interface-defining code?</h2>
<p>^ You know how you have some modules that are really only used one or two places, they're kinda internal, and you hope nobody looks at them too hard?</p>
<p>^ Interface-defining is the opposite of that. It's the hard boundaries of your module.</p>
<hr>
<p>From node's <code>events.js</code></p>
<div class="highlight highlight-source-js"><pre><span class="pl-c1">exports</span>.<span class="pl-smi">usingDomains</span> <span class="pl-k">=</span> <span class="pl-c1">false</span>;

<span class="pl-k">function</span> <span class="pl-en">EventEmitter</span>() { }
<span class="pl-c1">exports</span>.<span class="pl-smi">EventEmitter</span> <span class="pl-k">=</span> EventEmitter;

<span class="pl-smi">EventEmitter</span>.<span class="pl-c1">prototype</span>.<span class="pl-en">setMaxListeners</span> <span class="pl-k">=</span> <span class="pl-k">function</span> <span class="pl-en">setMaxListeners</span>(<span class="pl-smi">n</span>) { };
<span class="pl-smi">EventEmitter</span>.<span class="pl-c1">prototype</span>.<span class="pl-en">emit</span> <span class="pl-k">=</span> <span class="pl-k">function</span> <span class="pl-en">emit</span>(<span class="pl-smi">type</span>) { };
<span class="pl-smi">EventEmitter</span>.<span class="pl-c1">prototype</span>.<span class="pl-en">addListener</span> <span class="pl-k">=</span> <span class="pl-k">function</span> <span class="pl-en">addListener</span>(<span class="pl-smi">type</span>, <span class="pl-smi">listener</span>) { };
<span class="pl-smi">EventEmitter</span>.<span class="pl-c1">prototype</span>.<span class="pl-smi">on</span> <span class="pl-k">=</span> <span class="pl-smi">EventEmitter</span>.<span class="pl-c1">prototype</span>.<span class="pl-smi">addListener</span>;
<span class="pl-smi">EventEmitter</span>.<span class="pl-c1">prototype</span>.<span class="pl-en">once</span> <span class="pl-k">=</span> <span class="pl-k">function</span> <span class="pl-en">once</span>(<span class="pl-smi">type</span>, <span class="pl-smi">listener</span>) { };
<span class="pl-smi">EventEmitter</span>.<span class="pl-c1">prototype</span>.<span class="pl-en">removeListener</span> <span class="pl-k">=</span> <span class="pl-k">function</span> <span class="pl-en">removeListener</span>(<span class="pl-smi">type</span>, <span class="pl-smi">listener</span>) { };
<span class="pl-smi">EventEmitter</span>.<span class="pl-c1">prototype</span>.<span class="pl-en">removeAllListeners</span> <span class="pl-k">=</span> <span class="pl-k">function</span> <span class="pl-en">removeAllListeners</span>(<span class="pl-smi">type</span>) {};
<span class="pl-smi">EventEmitter</span>.<span class="pl-c1">prototype</span>.<span class="pl-en">listeners</span> <span class="pl-k">=</span> <span class="pl-k">function</span> <span class="pl-en">listeners</span>(<span class="pl-smi">type</span>) { };
<span class="pl-smi">EventEmitter</span>.<span class="pl-en">listenerCount</span> <span class="pl-k">=</span> <span class="pl-k">function</span>(<span class="pl-smi">emitter</span>, <span class="pl-smi">type</span>) { };</pre></div>
<p>^ We're defining the interface for <code>EventEmitter</code> here.</p>
<p>^ Some things to ask here are is this complete?  What guarantees does this make? Are internal details exposed?</p>
<p>^ If you have strong interface contracts, this is where you should expect to find them.</p>
<p>^ Like glue code, look for how errors are handled and exposed. Is that consistent? Does it distinguish errors due to internal inconsistency from errors because the user of the interface didn't understand it?</p>
<hr>
<h2><a id="user-content-implementation" class="anchor" aria-hidden="true" href="#implementation"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>Implementation</h2>
<hr>
<div class="highlight highlight-source-js"><pre>  <span class="pl-en">startRouting</span><span class="pl-k">:</span> <span class="pl-k">function</span>() {
    <span class="pl-c1">this</span>.<span class="pl-smi">router</span> <span class="pl-k">=</span> <span class="pl-c1">this</span>.<span class="pl-smi">router</span> <span class="pl-k">||</span> <span class="pl-c1">this</span>.<span class="pl-c1">constructor</span>.<span class="pl-en">map</span>(<span class="pl-c1">K</span>);

    <span class="pl-k">var</span> router <span class="pl-k">=</span> <span class="pl-c1">this</span>.<span class="pl-smi">router</span>;
    <span class="pl-k">var</span> location <span class="pl-k">=</span> <span class="pl-en">get</span>(<span class="pl-c1">this</span>, <span class="pl-s"><span class="pl-pds">'</span>location<span class="pl-pds">'</span></span>);
    <span class="pl-k">var</span> container <span class="pl-k">=</span> <span class="pl-c1">this</span>.<span class="pl-smi">container</span>;
    <span class="pl-k">var</span> self <span class="pl-k">=</span> <span class="pl-c1">this</span>;
    <span class="pl-k">var</span> initialURL <span class="pl-k">=</span> <span class="pl-en">get</span>(<span class="pl-c1">this</span>, <span class="pl-s"><span class="pl-pds">'</span>initialURL<span class="pl-pds">'</span></span>);
    <span class="pl-k">var</span> initialTransition;

    <span class="pl-c"><span class="pl-c">//</span> Allow the Location class to cancel the router setup while it refreshes</span>
    <span class="pl-c"><span class="pl-c">//</span> the page</span>
    <span class="pl-k">if</span> (<span class="pl-en">get</span>(location, <span class="pl-s"><span class="pl-pds">'</span>cancelRouterSetup<span class="pl-pds">'</span></span>)) {
      <span class="pl-k">return</span>;
    }

    <span class="pl-c1">this</span>.<span class="pl-en">_setupRouter</span>(router, location);

    <span class="pl-smi">container</span>.<span class="pl-en">register</span>(<span class="pl-s"><span class="pl-pds">'</span>view:default<span class="pl-pds">'</span></span>, _MetamorphView);
    <span class="pl-smi">container</span>.<span class="pl-en">register</span>(<span class="pl-s"><span class="pl-pds">'</span>view:toplevel<span class="pl-pds">'</span></span>, <span class="pl-smi">EmberView</span>.<span class="pl-en">extend</span>());

    <span class="pl-smi">location</span>.<span class="pl-en">onUpdateURL</span>(<span class="pl-k">function</span>(<span class="pl-smi">url</span>) {
      <span class="pl-smi">self</span>.<span class="pl-en">handleURL</span>(url);
    });

    <span class="pl-k">if</span> (<span class="pl-k">typeof</span> initialURL <span class="pl-k">===</span> <span class="pl-s"><span class="pl-pds">"</span>undefined<span class="pl-pds">"</span></span>) {
      initialURL <span class="pl-k">=</span> <span class="pl-smi">location</span>.<span class="pl-en">getURL</span>();
    }
    initialTransition <span class="pl-k">=</span> <span class="pl-c1">this</span>.<span class="pl-en">handleURL</span>(initialURL);
    <span class="pl-k">if</span> (initialTransition <span class="pl-k">&amp;&amp;</span> <span class="pl-smi">initialTransition</span>.<span class="pl-smi">error</span>) {
      <span class="pl-k">throw</span> <span class="pl-smi">initialTransition</span>.<span class="pl-smi">error</span>;
    }
  },</pre></div>
<p>From <code>Ember.Router</code></p>
<p>^ This is what that always needs more documentation about why and not so much about what.</p>
<p>^ Things to look for when reading here are how it fits into the larger whole.</p>
<p>^ What's coming from the public interface to this module? What needs validation? Are these variables going to contain what we think they contain? What other parts does this touch? What's the risk to changing it when adding new features? What might break? Do we have tests for that?</p>
<p>^ What's the lifetime of these variables? (this is an easy one: This looks really well designed and doesn't store needless state with a long lifetime.) Though maybe we should look at <code>_setupRouter</code>...</p>
<hr>
<h2><a id="user-content-process-entailment" class="anchor" aria-hidden="true" href="#process-entailment"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>Process entailment</h2>
<p>Or, looking forward: <em>How much is required to use this thing correctly?</em></p>
<p>and backward: <em>If we're here, what got us to this point?</em></p>
<p>^ It's pretty easy to see what functions call what other functions. However, the reverse is more interesting! So one of the things you can look for when reading source code, and in particular the implementation bits is look at what things have to happen to set up the state the process needs to be in to begin.</p>
<p>^ Is that state explicit, passed in via parameters? Is it assumed to be there, as an instance variable or property? Is there a single path to get there, with an obvious place that state is set up? Or is it diffuse?</p>
<hr>
<h2><a id="user-content-algorithms" class="anchor" aria-hidden="true" href="#algorithms"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>Algorithms</h2>
<p>^ So algorithmic code is a kind of special case of implementation code. It's not so exposed to the outside world, it's the meat of a program. Quite often it's business logic or the core processes of the software.</p>
<hr>
<div class="highlight highlight-source-js"><pre><span class="pl-k">function</span> <span class="pl-en">Grammar</span>(<span class="pl-smi">rules</span>) {
  <span class="pl-c"><span class="pl-c">//</span> Processing The Grammar</span>
  <span class="pl-c"><span class="pl-c">//</span></span>
  <span class="pl-c"><span class="pl-c">//</span> Here we begin defining a grammar given the raw rules, terminal</span>
  <span class="pl-c"><span class="pl-c">//</span> symbols, and symbolic references to rules</span>
  <span class="pl-c"><span class="pl-c">//</span></span>
  <span class="pl-c"><span class="pl-c">//</span> The input is a list of rules.</span>
  <span class="pl-c"><span class="pl-c">//</span></span>
  <span class="pl-c"><span class="pl-c">//</span> The input grammar is amended with a final rule, the 'accept' rule,</span>
  <span class="pl-c"><span class="pl-c">//</span> which if it spans the parse chart, means the entire grammar was</span>
  <span class="pl-c"><span class="pl-c">//</span> accepted. This is needed in the case of a nulling start symbol.</span>
  <span class="pl-smi">rules</span>.<span class="pl-c1">push</span>(<span class="pl-en">Rule</span>(<span class="pl-s"><span class="pl-pds">'</span>_accept<span class="pl-pds">'</span></span>, [<span class="pl-en">Ref</span>(<span class="pl-s"><span class="pl-pds">'</span>start<span class="pl-pds">'</span></span>)]));
  <span class="pl-smi">rules</span>.<span class="pl-smi">acceptRule</span> <span class="pl-k">=</span> <span class="pl-smi">rules</span>.<span class="pl-c1">length</span> <span class="pl-k">-</span> <span class="pl-c1">1</span>;</pre></div>
<p>This bit is from a parser engine I've been working on called <code>lotsawa</code>. More on the next slide.</p>
<p>^ It's been said a lot that good comments say why something is done or done that way, rather than what it's doing. Algorithms usually need more explanation of what's going on since if they were trivial, they'd probably be built into our standard library. Quite often to get good performance out of something, the exactly what-and-how matters a lot.</p>
<p>^ This is the stuff that those of you with CS degrees get to drool over (or maybe have traumatic memories of).</p>
<hr>
<div class="highlight highlight-source-js"><pre>  <span class="pl-c"><span class="pl-c">//</span> Build a list of all the symbols used in the grammar so they can be numbered instead of referred to</span>
  <span class="pl-c"><span class="pl-c">//</span> by name, and therefore their presence can be represented by a single bit in a set.</span>
  <span class="pl-k">function</span> <span class="pl-en">censusSymbols</span>() {
    <span class="pl-k">var</span> out <span class="pl-k">=</span> [];
    <span class="pl-smi">rules</span>.<span class="pl-c1">forEach</span>(<span class="pl-k">function</span>(<span class="pl-smi">r</span>) {
      <span class="pl-k">if</span> (<span class="pl-k">!</span><span class="pl-k">~</span><span class="pl-smi">out</span>.<span class="pl-c1">indexOf</span>(<span class="pl-smi">r</span>.<span class="pl-c1">name</span>)) <span class="pl-smi">out</span>.<span class="pl-c1">push</span>(<span class="pl-smi">r</span>.<span class="pl-c1">name</span>);

      <span class="pl-smi">r</span>.<span class="pl-smi">symbols</span>.<span class="pl-c1">forEach</span>(<span class="pl-k">function</span>(<span class="pl-smi">s</span>, <span class="pl-smi">i</span>) {
        <span class="pl-k">var</span> symNo <span class="pl-k">=</span> <span class="pl-smi">out</span>.<span class="pl-c1">indexOf</span>(<span class="pl-smi">s</span>.<span class="pl-c1">name</span>);
        <span class="pl-k">if</span> (<span class="pl-k">!</span><span class="pl-k">~</span><span class="pl-smi">out</span>.<span class="pl-c1">indexOf</span>(<span class="pl-smi">s</span>.<span class="pl-c1">name</span>)) {
          symNo <span class="pl-k">=</span> <span class="pl-smi">out</span>.<span class="pl-c1">length</span>;
          <span class="pl-smi">out</span>.<span class="pl-c1">push</span>(<span class="pl-smi">s</span>.<span class="pl-c1">name</span>);
        }

        <span class="pl-smi">r</span>.<span class="pl-smi">symbols</span>[i] <span class="pl-k">=</span> symNo;
      });

      <span class="pl-smi">r</span>.<span class="pl-smi">sym</span> <span class="pl-k">=</span> <span class="pl-smi">out</span>.<span class="pl-c1">indexOf</span>(<span class="pl-smi">r</span>.<span class="pl-c1">name</span>);
    });

    <span class="pl-k">return</span> out;
  }

  <span class="pl-smi">rules</span>.<span class="pl-smi">symbols</span> <span class="pl-k">=</span> <span class="pl-en">censusSymbols</span>();
</pre></div>
<p>Reads like a math paper, doesn't it?</p>
<p>^ One of the things that you usually need to see in algorithmic code is the actual data structures. This one is building a list of symbols and making sure there's no duplicates.</p>
<p>^ Look also for hints as to the running time of the algorithm. You can see in this part, I've got two loops. In Big-O notation, that's O(n * m), then you can see that there's an <code>indexOf</code> inside that. That's another loop in Javascript, so that actually adds another factor to the running time. (twice -- looks like I could make this more optimal by re-using one of the values here) Good thing this isn't the main part of the algorithm!</p>
<hr>
<h2><a id="user-content-configuration" class="anchor" aria-hidden="true" href="#configuration"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>Configuration</h2>
<p>^ The line between source code and configuration file is super thin. There's a constant tension between having a configuration be expressive and readable and direct.</p>
<hr>
<div class="highlight highlight-source-js"><pre><span class="pl-smi">app</span>.<span class="pl-en">configure</span>(<span class="pl-s"><span class="pl-pds">'</span>production<span class="pl-pds">'</span></span>, <span class="pl-s"><span class="pl-pds">'</span>staging<span class="pl-pds">'</span></span>, <span class="pl-k">function</span>() {
  <span class="pl-smi">app</span>.<span class="pl-en">enable</span>(<span class="pl-s"><span class="pl-pds">'</span>emails<span class="pl-pds">'</span></span>);
});

<span class="pl-smi">app</span>.<span class="pl-en">configure</span>(<span class="pl-s"><span class="pl-pds">'</span>test<span class="pl-pds">'</span></span>, <span class="pl-k">function</span>() {
  <span class="pl-smi">app</span>.<span class="pl-en">disable</span>(<span class="pl-s"><span class="pl-pds">'</span>emails<span class="pl-pds">'</span></span>);
});</pre></div>
<p>An example using Javascript for configuration.</p>
<p>^ What we can run into here is combinatorial explosion of options. How many environments do we configure? Then, how many things do we configure for a specific instance of that environment. It's really easy to go overboard and end up with all the possible permutations, and to have bugs that only show up in one of them. Keeping an eye out for how many degrees of freedom the configuration allows is super useful.</p>
<hr>
<div class="highlight highlight-source-js"><pre>    <span class="pl-s"><span class="pl-pds">"</span>express<span class="pl-pds">"</span></span><span class="pl-k">:</span> {
        <span class="pl-s"><span class="pl-pds">"</span>env<span class="pl-pds">"</span></span><span class="pl-k">:</span> <span class="pl-s"><span class="pl-pds">"</span><span class="pl-pds">"</span></span>, <span class="pl-c"><span class="pl-c">//</span> NOTE: `env` is managed by the framework. This value will be overwritten.</span>
        <span class="pl-s"><span class="pl-pds">"</span>x-powered-by<span class="pl-pds">"</span></span><span class="pl-k">:</span> <span class="pl-c1">false</span>,
        <span class="pl-s"><span class="pl-pds">"</span>views<span class="pl-pds">"</span></span><span class="pl-k">:</span> <span class="pl-s"><span class="pl-pds">"</span>path:./views<span class="pl-pds">"</span></span>,
        <span class="pl-s"><span class="pl-pds">"</span>mountpath<span class="pl-pds">"</span></span><span class="pl-k">:</span> <span class="pl-s"><span class="pl-pds">"</span>/<span class="pl-pds">"</span></span>
    },

    <span class="pl-s"><span class="pl-pds">"</span>middleware<span class="pl-pds">"</span></span><span class="pl-k">:</span> {

        <span class="pl-s"><span class="pl-pds">"</span>compress<span class="pl-pds">"</span></span><span class="pl-k">:</span> {
            <span class="pl-s"><span class="pl-pds">"</span>enabled<span class="pl-pds">"</span></span><span class="pl-k">:</span> <span class="pl-c1">false</span>,
            <span class="pl-s"><span class="pl-pds">"</span>priority<span class="pl-pds">"</span></span><span class="pl-k">:</span> <span class="pl-c1">10</span>,
            <span class="pl-s"><span class="pl-pds">"</span>module<span class="pl-pds">"</span></span><span class="pl-k">:</span> <span class="pl-s"><span class="pl-pds">"</span>compression<span class="pl-pds">"</span></span>
        },

        <span class="pl-s"><span class="pl-pds">"</span>favicon<span class="pl-pds">"</span></span><span class="pl-k">:</span> {
            <span class="pl-s"><span class="pl-pds">"</span>enabled<span class="pl-pds">"</span></span><span class="pl-k">:</span> <span class="pl-c1">false</span>,
            <span class="pl-s"><span class="pl-pds">"</span>priority<span class="pl-pds">"</span></span><span class="pl-k">:</span> <span class="pl-c1">30</span>,
            <span class="pl-s"><span class="pl-pds">"</span>module<span class="pl-pds">"</span></span><span class="pl-k">:</span> {
                <span class="pl-s"><span class="pl-pds">"</span>name<span class="pl-pds">"</span></span><span class="pl-k">:</span> <span class="pl-s"><span class="pl-pds">"</span>serve-favicon<span class="pl-pds">"</span></span>,
                <span class="pl-s"><span class="pl-pds">"</span>arguments<span class="pl-pds">"</span></span><span class="pl-k">:</span> [ <span class="pl-s"><span class="pl-pds">"</span>resolve:kraken-js/public/favicon.ico<span class="pl-pds">"</span></span> ]
            }
        },
</pre></div>
<p>A bit of <code>kraken</code> config file.</p>
<p>^ Kraken took a 'low power language' approach to configuration and chose JSON. A little more "configuration" and a little less "source code". One of the goals was keeping that combinatorial explosion under control. There's a reason a lot of tools use simple key-value pairs or ini-style files for configuration, even though they're not terribly expressive.</p>
<hr>
<p>Configuration source code has some interesting and unique constraints that are worth looking for.</p>
<ul>
<li>Lifetime</li>
<li>Machine writability</li>
<li>Responsible people vary a lot more</li>
<li>Have to fit in weird places like environment variables</li>
<li>Often store security-sensitive information</li>
</ul>
<hr>
<h2><a id="user-content-tasking" class="anchor" aria-hidden="true" href="#tasking"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>Tasking</h2>
<hr>
<p>What do charging 50 credit cards, building a complex piece of software with a compiler and build tools, and sending 100 emails have in common?</p>
<p>^ Transactionality. Often, some piece of the system needs to happen exactly once, and not at all if there's an error. A compiler that leaves bad build products around is a great source of bugs. Double charging customers is bad. Flooding someone's inbox because of a retry cycle is terrible.</p>
<p>^ Resumabilty. A need to continue where they left off given the state of the system.</p>
<p>^ Sequentiality. If they're not strictly linear processes, there's usually a very directed flow through the code. Loops tend to be big ones, around the whole shebang.</p>
<hr>
<h2><a id="user-content-reading-messy-code" class="anchor" aria-hidden="true" href="#reading-messy-code"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>Reading Messy Code</h2>
<hr>
<p>So how do you deal with this?</p>
<div class="highlight highlight-source-js"><pre>      <span class="pl-smi">DuplexCombination</span>.<span class="pl-c1">prototype</span>.<span class="pl-en">on</span> <span class="pl-k">=</span> <span class="pl-k">function</span>(<span class="pl-smi">ev</span>, <span class="pl-smi">fn</span>) {
    <span class="pl-k">switch</span> (ev) {
  <span class="pl-k">case</span> <span class="pl-s"><span class="pl-pds">'</span>data<span class="pl-pds">'</span></span>:
  <span class="pl-k">case</span> <span class="pl-s"><span class="pl-pds">'</span>end<span class="pl-pds">'</span></span>:
  <span class="pl-k">case</span> <span class="pl-s"><span class="pl-pds">'</span>readable<span class="pl-pds">'</span></span>:
<span class="pl-c1">this</span>.<span class="pl-smi">reader</span>.<span class="pl-en">on</span>(ev, fn);
<span class="pl-k">return</span> <span class="pl-c1">this</span>
  <span class="pl-k">case</span> <span class="pl-s"><span class="pl-pds">'</span>drain<span class="pl-pds">'</span></span>:
  <span class="pl-k">case</span> <span class="pl-s"><span class="pl-pds">'</span>finish<span class="pl-pds">'</span></span>:
<span class="pl-c1">this</span>.<span class="pl-smi">writer</span>.<span class="pl-en">on</span>(ev, fn);
<span class="pl-k">return</span> <span class="pl-c1">this</span>
  <span class="pl-k">default</span>:
<span class="pl-k">return</span> <span class="pl-smi">Duplex</span>.<span class="pl-c1">prototype</span>.<span class="pl-smi">on</span>.<span class="pl-c1">call</span>(<span class="pl-c1">this</span>, ev, fn);
    }
      };</pre></div>
<p>You are seeing that right. That's reverse indendation. Blame Isaac.</p>
<hr>
<h2><a id="user-content-rose-tinted-glasses" class="anchor" aria-hidden="true" href="#rose-tinted-glasses"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>Rose tinted glasses!</h2>
<p><code>standard -F dc.js</code></p>
<div class="highlight highlight-source-js"><pre><span class="pl-smi">DuplexCombination</span>.<span class="pl-c1">prototype</span>.<span class="pl-en">on</span> <span class="pl-k">=</span> <span class="pl-k">function</span> (<span class="pl-smi">ev</span>, <span class="pl-smi">fn</span>) {
  <span class="pl-k">switch</span> (ev) {
    <span class="pl-k">case</span> <span class="pl-s"><span class="pl-pds">'</span>data<span class="pl-pds">'</span></span>:
    <span class="pl-k">case</span> <span class="pl-s"><span class="pl-pds">'</span>end<span class="pl-pds">'</span></span>:
    <span class="pl-k">case</span> <span class="pl-s"><span class="pl-pds">'</span>readable<span class="pl-pds">'</span></span>:
      <span class="pl-c1">this</span>.<span class="pl-smi">reader</span>.<span class="pl-en">on</span>(ev, fn)
      <span class="pl-k">return</span> <span class="pl-c1">this</span>
    <span class="pl-k">case</span> <span class="pl-s"><span class="pl-pds">'</span>drain<span class="pl-pds">'</span></span>:
    <span class="pl-k">case</span> <span class="pl-s"><span class="pl-pds">'</span>finish<span class="pl-pds">'</span></span>:
      <span class="pl-c1">this</span>.<span class="pl-smi">writer</span>.<span class="pl-en">on</span>(ev, fn)
      <span class="pl-k">return</span> <span class="pl-c1">this</span>
    <span class="pl-k">default</span>:
      <span class="pl-k">return</span> <span class="pl-smi">Duplex</span>.<span class="pl-c1">prototype</span>.<span class="pl-smi">on</span>.<span class="pl-c1">call</span>(<span class="pl-c1">this</span>, ev, fn)
  }
}</pre></div>
<p>It's okay to use tools while reading!</p>
<hr>
<p>How do you read this?</p>
<div class="highlight highlight-source-js"><pre>(<span class="pl-k">function</span>(<span class="pl-smi">t</span>,<span class="pl-smi">e</span>){<span class="pl-k">if</span>(<span class="pl-k">typeof</span> define<span class="pl-k">===</span><span class="pl-s"><span class="pl-pds">"</span>function<span class="pl-pds">"</span></span><span class="pl-k">&amp;&amp;</span><span class="pl-smi">define</span>.<span class="pl-smi">amd</span>){<span class="pl-en">define</span>([<span class="pl-s"><span class="pl-pds">"</span>underscore<span class="pl-pds">"</span></span>,<span class="pl-s"><span class="pl-pds">"</span></span>
<span class="pl-s">jquery<span class="pl-pds">"</span></span>,<span class="pl-s"><span class="pl-pds">"</span>exports<span class="pl-pds">"</span></span>],<span class="pl-k">function</span>(<span class="pl-smi">i</span>,<span class="pl-smi">r</span>,<span class="pl-smi">s</span>){<span class="pl-smi">t</span>.<span class="pl-smi">Backbone</span><span class="pl-k">=</span><span class="pl-en">e</span>(t,s,i,r)})}<span class="pl-k">else</span> <span class="pl-k">if</span>(<span class="pl-k">typeof</span> <span class="pl-k">export</span>
s<span class="pl-k">!==</span><span class="pl-s"><span class="pl-pds">"</span>undefined<span class="pl-pds">"</span></span>){<span class="pl-k">var</span> i<span class="pl-k">=</span><span class="pl-c1">require</span>(<span class="pl-s"><span class="pl-pds">"</span>underscore<span class="pl-pds">"</span></span>);<span class="pl-en">e</span>(t,<span class="pl-c1">exports</span>,i)}<span class="pl-k">else</span>{<span class="pl-smi">t</span>.<span class="pl-smi">Backbone</span><span class="pl-k">=</span><span class="pl-en">e</span>(t,
{},<span class="pl-smi">t</span>.<span class="pl-smi">_</span>,<span class="pl-smi">t</span>.<span class="pl-smi">jQuery</span><span class="pl-k">||</span><span class="pl-smi">t</span>.<span class="pl-smi">Zepto</span><span class="pl-k">||</span><span class="pl-smi">t</span>.<span class="pl-smi">ender</span><span class="pl-k">||</span><span class="pl-smi">t</span>.<span class="pl-smi">$</span>)}})(<span class="pl-c1">this</span>,<span class="pl-k">function</span>(<span class="pl-smi">t</span>,<span class="pl-smi">e</span>,<span class="pl-smi">i</span>,<span class="pl-smi">r</span>){<span class="pl-k">var</span> s<span class="pl-k">=</span><span class="pl-smi">t</span>.<span class="pl-smi">Backbo</span>
ne;<span class="pl-k">var</span> n<span class="pl-k">=</span>[];<span class="pl-k">var</span> a<span class="pl-k">=</span><span class="pl-smi">n</span>.<span class="pl-smi">push</span>;<span class="pl-k">var</span> o<span class="pl-k">=</span><span class="pl-smi">n</span>.<span class="pl-smi">slice</span>;<span class="pl-k">var</span> h<span class="pl-k">=</span><span class="pl-smi">n</span>.<span class="pl-smi">splice</span>;<span class="pl-smi">e</span>.<span class="pl-c1">VERSION</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">"</span>1.1.2<span class="pl-pds">"</span></span>;<span class="pl-smi">e</span>.<span class="pl-smi">$</span><span class="pl-k">=</span>r;e.
<span class="pl-en">noConflict</span><span class="pl-k">=</span><span class="pl-k">function</span>(){<span class="pl-smi">t</span>.<span class="pl-smi">Backbone</span><span class="pl-k">=</span>s;<span class="pl-k">return</span> <span class="pl-c1">this</span>};<span class="pl-smi">e</span>.<span class="pl-smi">emulateHTTP</span><span class="pl-k">=</span><span class="pl-c1">false</span>;<span class="pl-smi">e</span>.<span class="pl-smi">emulateJSO</span>
<span class="pl-c1">N</span><span class="pl-k">=</span><span class="pl-c1">false</span>;<span class="pl-k">var</span> u<span class="pl-k">=</span><span class="pl-smi">e</span>.<span class="pl-smi">Events</span><span class="pl-k">=</span>{<span class="pl-en">on</span><span class="pl-k">:</span><span class="pl-k">function</span>(<span class="pl-smi">t</span>,<span class="pl-smi">e</span>,<span class="pl-smi">i</span>){<span class="pl-k">if</span>(<span class="pl-k">!</span><span class="pl-en">c</span>(<span class="pl-c1">this</span>,<span class="pl-s"><span class="pl-pds">"</span>on<span class="pl-pds">"</span></span>,t,[e,i])<span class="pl-k">||!</span>e)<span class="pl-k">return</span> t
his;<span class="pl-c1">this</span>.<span class="pl-smi">_events</span><span class="pl-k">||</span>(<span class="pl-c1">this</span>.<span class="pl-smi">_events</span><span class="pl-k">=</span>{});<span class="pl-k">var</span> r<span class="pl-k">=</span><span class="pl-c1">this</span>.<span class="pl-smi">_events</span>[t]<span class="pl-k">||</span>(<span class="pl-c1">this</span>.<span class="pl-smi">_events</span>[t]<span class="pl-k">=</span>[]);
<span class="pl-smi">r</span>.<span class="pl-c1">push</span>({callback<span class="pl-k">:</span>e,context<span class="pl-k">:</span>i,ctx<span class="pl-k">:</span>i<span class="pl-k">||</span><span class="pl-c1">this</span>});<span class="pl-k">return</span> <span class="pl-c1">this</span>},<span class="pl-en">once</span><span class="pl-k">:</span><span class="pl-k">function</span>(<span class="pl-smi">t</span>,<span class="pl-smi">e</span>,<span class="pl-smi">r</span>){<span class="pl-k">if</span>(
<span class="pl-k">!</span><span class="pl-en">c</span>(<span class="pl-c1">this</span>,<span class="pl-s"><span class="pl-pds">"</span>once<span class="pl-pds">"</span></span>,t,[e,r])<span class="pl-k">||!</span>e)<span class="pl-k">return</span> <span class="pl-c1">this</span>;<span class="pl-k">var</span> s<span class="pl-k">=</span><span class="pl-c1">this</span>;<span class="pl-k">var</span> n<span class="pl-k">=</span><span class="pl-smi">i</span>.<span class="pl-en">once</span>(<span class="pl-k">function</span>(){<span class="pl-smi">s</span>.<span class="pl-smi">off</span>
(t,n);<span class="pl-smi">e</span>.<span class="pl-c1">apply</span>(<span class="pl-c1">this</span>,<span class="pl-c1">arguments</span>)});<span class="pl-smi">n</span>.<span class="pl-smi">_callback</span><span class="pl-k">=</span>e;<span class="pl-k">return</span> <span class="pl-c1">this</span>.<span class="pl-en">on</span>(t,n,r)},off<span class="pl-k">:</span>functio
<span class="pl-en">n</span>(<span class="pl-smi">t</span>,<span class="pl-smi">e</span>,<span class="pl-smi">r</span>){<span class="pl-k">var</span> s,n,a,o,h,u,l,f;<span class="pl-k">if</span>(<span class="pl-k">!</span><span class="pl-c1">this</span>.<span class="pl-smi">_events</span><span class="pl-k">||!</span><span class="pl-en">c</span>(<span class="pl-c1">this</span>,<span class="pl-s"><span class="pl-pds">"</span>off<span class="pl-pds">"</span></span>,t,[e,r]))<span class="pl-k">return</span> thi
s;<span class="pl-k">if</span>(<span class="pl-k">!</span>t<span class="pl-k">&amp;&amp;!</span>e<span class="pl-k">&amp;&amp;!</span>r){<span class="pl-c1">this</span>.<span class="pl-smi">_events</span><span class="pl-k">=</span><span class="pl-k">void</span> <span class="pl-c1">0</span>;<span class="pl-k">return</span> <span class="pl-c1">this</span>}o<span class="pl-k">=</span>t<span class="pl-k">?</span>[t]<span class="pl-k">:</span><span class="pl-smi">i</span>.<span class="pl-c1">keys</span>(<span class="pl-c1">this</span>.<span class="pl-smi">_events</span>);fo
<span class="pl-en">r</span>(<span class="pl-smi">h</span><span class="pl-k">=</span><span class="pl-c1">0</span>,<span class="pl-smi">u</span><span class="pl-k">=</span><span class="pl-smi">o</span>.<span class="pl-c1">length</span>;<span class="pl-smi">h</span><span class="pl-k">&lt;</span><span class="pl-smi">u</span>;<span class="pl-smi">h</span><span class="pl-k">++</span>){t<span class="pl-k">=</span>o[h];<span class="pl-k">if</span>(a<span class="pl-k">=</span><span class="pl-c1">this</span>.<span class="pl-smi">_events</span>[t]){<span class="pl-c1">this</span>.<span class="pl-smi">_events</span>[t]<span class="pl-k">=</span>s<span class="pl-k">=</span>[];<span class="pl-k">if</span>(e
<span class="pl-k">||</span>r){<span class="pl-k">for</span>(l<span class="pl-k">=</span><span class="pl-c1">0</span>,f<span class="pl-k">=</span><span class="pl-smi">a</span>.<span class="pl-c1">length</span>;l<span class="pl-k">&lt;</span>f;l<span class="pl-k">++</span>){n<span class="pl-k">=</span>a[l];<span class="pl-k">if</span>(e<span class="pl-k">&amp;&amp;</span>e<span class="pl-k">!==</span><span class="pl-smi">n</span>.<span class="pl-smi">callback</span><span class="pl-k">&amp;&amp;</span>e<span class="pl-k">!==</span><span class="pl-smi">n</span>.<span class="pl-smi">callback</span>.<span class="pl-smi">_ca</span>
llback<span class="pl-k">||</span>r<span class="pl-k">&amp;&amp;</span>r<span class="pl-k">!==</span><span class="pl-smi">n</span>.<span class="pl-smi">context</span>){<span class="pl-smi">s</span>.<span class="pl-c1">push</span>(n)}}}<span class="pl-k">if</span>(<span class="pl-k">!</span><span class="pl-smi">s</span>.<span class="pl-c1">length</span>)<span class="pl-k">delete</span> <span class="pl-c1">this</span>.<span class="pl-smi">_events</span>[t]}}retur
n <span class="pl-c1">this</span>},<span class="pl-en">trigger</span><span class="pl-k">:</span><span class="pl-k">function</span>(<span class="pl-smi">t</span>){<span class="pl-k">if</span>(<span class="pl-k">!</span><span class="pl-c1">this</span>.<span class="pl-smi">_events</span>)<span class="pl-k">return</span> <span class="pl-c1">this</span>;<span class="pl-k">var</span> e<span class="pl-k">=</span><span class="pl-smi">o</span>.<span class="pl-c1">call</span>(<span class="pl-c1">arguments</span>,
<span class="pl-c1">1</span>);<span class="pl-k">if</span>(<span class="pl-k">!</span><span class="pl-en">c</span>(<span class="pl-c1">this</span>,<span class="pl-s"><span class="pl-pds">"</span>trigger<span class="pl-pds">"</span></span>,t,e))<span class="pl-k">return</span> <span class="pl-c1">this</span>;<span class="pl-k">var</span> i<span class="pl-k">=</span><span class="pl-c1">this</span>.<span class="pl-smi">_events</span>[t];<span class="pl-k">var</span> r<span class="pl-k">=</span><span class="pl-c1">this</span>.<span class="pl-smi">_event</span>
<span class="pl-smi">s</span>.<span class="pl-c1">all</span>;<span class="pl-k">if</span>(i)<span class="pl-en">f</span>(i,e);<span class="pl-k">if</span>(r)<span class="pl-en">f</span>(r,<span class="pl-c1">arguments</span>);<span class="pl-k">return</span> <span class="pl-c1">this</span>},<span class="pl-en">stopListening</span><span class="pl-k">:</span><span class="pl-k">function</span>(<span class="pl-smi">t</span>,<span class="pl-smi">e</span>,<span class="pl-smi">r</span>)
{<span class="pl-k">var</span> s<span class="pl-k">=</span><span class="pl-c1">this</span>.<span class="pl-smi">_listeningTo</span>;<span class="pl-k">if</span>(<span class="pl-k">!</span>s)<span class="pl-k">return</span> <span class="pl-c1">this</span>;<span class="pl-k">var</span> n<span class="pl-k">=</span><span class="pl-k">!</span>e<span class="pl-k">&amp;&amp;!</span>r;<span class="pl-k">if</span>(<span class="pl-k">!</span>r<span class="pl-k">&amp;&amp;</span><span class="pl-k">typeof</span> e<span class="pl-k">===</span><span class="pl-s"><span class="pl-pds">"</span><span class="pl-ii">objec</span></span></pre></div>
<hr>
<p><code>uglifyjs -b &lt; backbone-min.js</code></p>
<div class="highlight highlight-source-js"><pre>(<span class="pl-k">function</span>(<span class="pl-smi">t</span>, <span class="pl-smi">e</span>) {
    <span class="pl-k">if</span> (<span class="pl-k">typeof</span> define <span class="pl-k">===</span> <span class="pl-s"><span class="pl-pds">"</span>function<span class="pl-pds">"</span></span> <span class="pl-k">&amp;&amp;</span> <span class="pl-smi">define</span>.<span class="pl-smi">amd</span>) {
        <span class="pl-en">define</span>([ <span class="pl-s"><span class="pl-pds">"</span>underscore<span class="pl-pds">"</span></span>, <span class="pl-s"><span class="pl-pds">"</span>jquery<span class="pl-pds">"</span></span>, <span class="pl-s"><span class="pl-pds">"</span>exports<span class="pl-pds">"</span></span> ], <span class="pl-k">function</span>(<span class="pl-smi">i</span>, <span class="pl-smi">r</span>, <span class="pl-smi">s</span>) {
            <span class="pl-smi">t</span>.<span class="pl-smi">Backbone</span> <span class="pl-k">=</span> <span class="pl-en">e</span>(t, s, i, r);
        });
    } <span class="pl-k">else</span> <span class="pl-k">if</span> (<span class="pl-k">typeof</span> <span class="pl-c1">exports</span> <span class="pl-k">!==</span> <span class="pl-s"><span class="pl-pds">"</span>undefined<span class="pl-pds">"</span></span>) {
        <span class="pl-k">var</span> i <span class="pl-k">=</span> <span class="pl-c1">require</span>(<span class="pl-s"><span class="pl-pds">"</span>underscore<span class="pl-pds">"</span></span>);
        <span class="pl-en">e</span>(t, <span class="pl-c1">exports</span>, i);
    } <span class="pl-k">else</span> {
        <span class="pl-smi">t</span>.<span class="pl-smi">Backbone</span> <span class="pl-k">=</span> <span class="pl-en">e</span>(t, {}, <span class="pl-smi">t</span>.<span class="pl-smi">_</span>, <span class="pl-smi">t</span>.<span class="pl-smi">jQuery</span> <span class="pl-k">||</span> <span class="pl-smi">t</span>.<span class="pl-smi">Zepto</span> <span class="pl-k">||</span> <span class="pl-smi">t</span>.<span class="pl-smi">ender</span> <span class="pl-k">||</span> <span class="pl-smi">t</span>.<span class="pl-smi">$</span>);
    }
})(<span class="pl-c1">this</span>, <span class="pl-k">function</span>(<span class="pl-smi">t</span>, <span class="pl-smi">e</span>, <span class="pl-smi">i</span>, <span class="pl-smi">r</span>) {
    <span class="pl-k">var</span> s <span class="pl-k">=</span> <span class="pl-smi">t</span>.<span class="pl-smi">Backbone</span>;
    <span class="pl-k">var</span> n <span class="pl-k">=</span> [];
    <span class="pl-k">var</span> a <span class="pl-k">=</span> <span class="pl-smi">n</span>.<span class="pl-smi">push</span>;
    <span class="pl-k">var</span> o <span class="pl-k">=</span> <span class="pl-smi">n</span>.<span class="pl-smi">slice</span>;
    <span class="pl-k">var</span> h <span class="pl-k">=</span> <span class="pl-smi">n</span>.<span class="pl-smi">splice</span>;
    <span class="pl-smi">e</span>.<span class="pl-c1">VERSION</span> <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">"</span>1.1.2<span class="pl-pds">"</span></span>;
    <span class="pl-smi">e</span>.<span class="pl-smi">$</span> <span class="pl-k">=</span> r;
    <span class="pl-smi">e</span>.<span class="pl-en">noConflict</span> <span class="pl-k">=</span> <span class="pl-k">function</span>() {</pre></div>
<hr>
<h2><a id="user-content-human-parts" class="anchor" aria-hidden="true" href="#human-parts"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>Human Parts</h2>
<p>Or: <em>guessing intent is dangerous but you learn so much</em></p>
<hr>
<p>There's a lot of tricks for figuring out what the author of something meant.</p>
<hr>
<h2><a id="user-content-look-for-guards-and-coercions" class="anchor" aria-hidden="true" href="#look-for-guards-and-coercions"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>Look for guards and coercions</h2>
<div class="highlight highlight-source-js"><pre><span class="pl-k">if</span> (<span class="pl-k">typeof</span> arg <span class="pl-k">!=</span> <span class="pl-s"><span class="pl-pds">'</span>number<span class="pl-pds">'</span></span>) <span class="pl-k">throw</span> <span class="pl-k">new</span> <span class="pl-en">TypeError</span>(<span class="pl-s"><span class="pl-pds">"</span>arg must be a number<span class="pl-pds">"</span></span>);</pre></div>
<p>Looks like the domain of whatever function we're in is 'numbers'.</p>
<hr>
<div class="highlight highlight-source-js"><pre>arg <span class="pl-k">=</span> <span class="pl-c1">Number</span>(arg)</pre></div>
<p>Coerce things to numeric. Same domain as above, but doesn't reject errors via exceptions. There might be <code>NaN</code>s though. Probably smart to read and check if there's comparisons that will be false against those.</p>
<hr>
<h2><a id="user-content-look-for-defaults" class="anchor" aria-hidden="true" href="#look-for-defaults"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>Look for defaults</h2>
<div class="highlight highlight-source-js"><pre>arg <span class="pl-k">=</span> arg <span class="pl-k">||</span> {}</pre></div>
<p>Default to an empty object.</p>
<div class="highlight highlight-source-js"><pre>arg <span class="pl-k">=</span> (arg <span class="pl-k">==</span> <span class="pl-c1">null</span> <span class="pl-k">?</span> <span class="pl-c1">true</span> <span class="pl-k">:</span> arg)</pre></div>
<p>Default to true only if a value wasn't explicitly passed.</p>
<hr>
<h2><a id="user-content-look-for-layers" class="anchor" aria-hidden="true" href="#look-for-layers"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>Look for layers</h2>
<p><code>req</code> and <code>res</code> from Express are tied to the web; how deep do they go?</p>
<p>Is there an interface boundary you can find?</p>
<hr>
<h2><a id="user-content-look-for-tracing" class="anchor" aria-hidden="true" href="#look-for-tracing"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>Look for tracing</h2>
<p>Are there inspection points?</p>
<p>Debug logs?</p>
<p>Do those form a complete narrative? Or are they ad-hoc leftovers from the last few bugs?</p>
<hr>
<h2><a id="user-content-look-for-reflexivity" class="anchor" aria-hidden="true" href="#look-for-reflexivity"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>Look for reflexivity</h2>
<p>Are identifiers being dynamically generated?</p>
<p>Is there <code>eval</code>? Metaprogramming? New function creation?</p>
<p><code>func.toString()</code> is your friend!</p>
<hr>
<h2><a id="user-content-look-at-lifetimes" class="anchor" aria-hidden="true" href="#look-at-lifetimes"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>Look at lifetimes</h2>
<ul>
<li>Who initializes this?</li>
<li>When does it change?</li>
<li>Who changes it?</li>
<li>Is this information somewhere else in the mean time?</li>
<li>Is it ever inconsistent?</li>
</ul>
<p>^ Somewhere, someone typed the value you see into a keyboard, generated it from a random number generator, or computed it and saved it.</p>
<p>^ Somewhere else, some time else, that value will affect some human or humans. Who are these people?</p>
<p>^ What or who chooses who they are?</p>
<p>^ Is that value ever going to change?</p>
<p>^ Who changes it?</p>
<hr>
<h2><a id="user-content-look-for-hidden-state-machines" class="anchor" aria-hidden="true" href="#look-for-hidden-state-machines"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>Look for hidden state machines</h2>
<p>^ Sometimes boolean variables get used together as a decomposed state machine</p>
<p>^ For example, the variables <code>isReadied</code> and <code>isFinished</code> might show a state machine like so:</p>
<div class="highlight highlight-source-js"><pre><span class="pl-k">var</span> isReadied <span class="pl-k">=</span> <span class="pl-c1">false</span>;
<span class="pl-k">var</span> isFinished <span class="pl-k">=</span> <span class="pl-c1">false</span>;</pre></div>
<p>Or</p>
<p><code>START -&gt; READY -&gt; FINISHED</code></p>
<hr>
<h2><a id="user-content-look-for-hidden-state-machines-1" class="anchor" aria-hidden="true" href="#look-for-hidden-state-machines-1"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>Look for hidden state machines</h2>
<pre><code>isReadied | isFinished | state
----------|------------|------------
false     | false      | START
false     | true       | invalid
true      | false      | READY
true      | true       | FINISHED
</code></pre>
<p>^ Note that they can also express the state <code>!isReadied &amp;&amp; isFinished</code> -- which might be an interesting source of bugs, if something can end up at the finished state without first being ready.</p>
<hr>
<h2><a id="user-content-look-for-composition-and-inheritance" class="anchor" aria-hidden="true" href="#look-for-composition-and-inheritance"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>Look for composition and inheritance</h2>
<p>Is this made of parts I can recognize? Do those parts have names?</p>
<hr>
<h2><a id="user-content-look-for-common-operations" class="anchor" aria-hidden="true" href="#look-for-common-operations"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>Look for common operations</h2>
<p><code>map</code>.</p>
<p><code>reduce</code>.</p>
<p>cross-join.</p>
<hr>
<p>It's time to go read some source code.</p>
<p>Enjoy!</p>
</article>
  </div>

    </div>

  

  <details class="details-reset details-overlay details-overlay-dark">
    <summary data-hotkey="l" aria-label="Jump to line"></summary>
    <details-dialog class="Box Box--overlay d-flex flex-column anim-fade-in fast linejump" aria-label="Jump to line">
      <!-- '"` --><!-- </textarea></xmp> --></option></form><form class="js-jump-to-line-form Box-body d-flex" action="" accept-charset="UTF-8" method="get"><input name="utf8" type="hidden" value="&#x2713;" />
        <input class="form-control flex-auto mr-3 linejump-input js-jump-to-line-field" type="text" placeholder="Jump to line&hellip;" aria-label="Jump to line" autofocus>
        <button type="submit" class="btn" data-close-dialog>Go</button>
</form>    </details-dialog>
  </details>


  </div>
  <div class="modal-backdrop js-touch-events"></div>
</div>

    </div>
  </div>

  </div>

        
<div class="footer container-lg px-3" role="contentinfo">
  <div class="position-relative d-flex flex-justify-between pt-6 pb-2 mt-6 f6 text-gray border-top border-gray-light ">
    <ul class="list-style-none d-flex flex-wrap ">
      <li class="mr-3">&copy; 2018 <span title="0.10355s from unicorn-77c89cc58d-lfx75">GitHub</span>, Inc.</li>
        <li class="mr-3"><a data-ga-click="Footer, go to terms, text:terms" href="https://github.com/site/terms">Terms</a></li>
        <li class="mr-3"><a data-ga-click="Footer, go to privacy, text:privacy" href="https://github.com/site/privacy">Privacy</a></li>
        <li class="mr-3"><a href="https://help.github.com/articles/github-security/" data-ga-click="Footer, go to security, text:security">Security</a></li>
        <li class="mr-3"><a href="https://status.github.com/" data-ga-click="Footer, go to status, text:status">Status</a></li>
        <li><a data-ga-click="Footer, go to help, text:help" href="https://help.github.com">Help</a></li>
    </ul>

    <a aria-label="Homepage" title="GitHub" class="footer-octicon mr-lg-4" href="https://github.com">
      <svg height="24" class="octicon octicon-mark-github" viewBox="0 0 16 16" version="1.1" width="24" aria-hidden="true"><path fill-rule="evenodd" d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0 0 16 8c0-4.42-3.58-8-8-8z"/></svg>
</a>
   <ul class="list-style-none d-flex flex-wrap ">
        <li class="mr-3"><a data-ga-click="Footer, go to contact, text:contact" href="https://github.com/contact">Contact GitHub</a></li>
        <li class="mr-3"><a href="https://github.com/pricing" data-ga-click="Footer, go to Pricing, text:Pricing">Pricing</a></li>
      <li class="mr-3"><a href="https://developer.github.com" data-ga-click="Footer, go to api, text:api">API</a></li>
      <li class="mr-3"><a href="https://training.github.com" data-ga-click="Footer, go to training, text:training">Training</a></li>
        <li class="mr-3"><a href="https://blog.github.com" data-ga-click="Footer, go to blog, text:blog">Blog</a></li>
        <li><a data-ga-click="Footer, go to about, text:about" href="https://github.com/about">About</a></li>

    </ul>
  </div>
  <div class="d-flex flex-justify-center pb-6">
    <span class="f6 text-gray-light"></span>
  </div>
</div>



  <div id="ajax-error-message" class="ajax-error-message flash flash-error">
    <svg class="octicon octicon-alert" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M8.893 1.5c-.183-.31-.52-.5-.887-.5s-.703.19-.886.5L.138 13.499a.98.98 0 0 0 0 1.001c.193.31.53.501.886.501h13.964c.367 0 .704-.19.877-.5a1.03 1.03 0 0 0 .01-1.002L8.893 1.5zm.133 11.497H6.987v-2.003h2.039v2.003zm0-3.004H6.987V5.987h2.039v4.006z"/></svg>
    <button type="button" class="flash-close js-ajax-error-dismiss" aria-label="Dismiss error">
      <svg class="octicon octicon-x" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.48 8l3.75 3.75-1.48 1.48L6 9.48l-3.75 3.75-1.48-1.48L4.52 8 .77 4.25l1.48-1.48L6 6.52l3.75-3.75 1.48 1.48L7.48 8z"/></svg>
    </button>
    You can’t perform that action at this time.
  </div>


    <script crossorigin="anonymous" integrity="sha512-mal0oz3cFcr4OqIE2eo7Pmax6HtpOKvQfO4vqg9JuCb+iaf4H3KUP9Aryp4oP5mSMgEYUOwgBOAL6MTFaeCZ3w==" type="application/javascript" src="https://assets-cdn.github.com/assets/compat-3c69a4d015c4208bce7a9d5e4e15a914.js"></script>
    <script crossorigin="anonymous" integrity="sha512-MvNlmXbTAwL0N0zMxw8W6vtjWLf0QFvwVzvN8rZIJNdzFy9OJp2d4LQD9WA2rDNcHewz0PB9x/0G0Z9FOuUWgw==" type="application/javascript" src="https://assets-cdn.github.com/assets/frameworks-a2f69f341e3df821fdcb56e335ef9920.js"></script>
    
    <script crossorigin="anonymous" async="async" integrity="sha512-ixxvBZF3eRHUBFtQhqjNyIJRouOkAqo1Glgy607wMwbpAT1Gu/1tGo5impwGiQi9DBWBeaXnVFEXmNTyPZjT3g==" type="application/javascript" src="https://assets-cdn.github.com/assets/github-1f0ca6fc0ad418e21430c85ad0f2544d.js"></script>
    
    
    
  <div class="js-stale-session-flash stale-session-flash flash flash-warn flash-banner d-none">
    <svg class="octicon octicon-alert" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M8.893 1.5c-.183-.31-.52-.5-.887-.5s-.703.19-.886.5L.138 13.499a.98.98 0 0 0 0 1.001c.193.31.53.501.886.501h13.964c.367 0 .704-.19.877-.5a1.03 1.03 0 0 0 .01-1.002L8.893 1.5zm.133 11.497H6.987v-2.003h2.039v2.003zm0-3.004H6.987V5.987h2.039v4.006z"/></svg>
    <span class="signed-in-tab-flash">You signed in with another tab or window. <a href="">Reload</a> to refresh your session.</span>
    <span class="signed-out-tab-flash">You signed out in another tab or window. <a href="">Reload</a> to refresh your session.</span>
  </div>
  <div class="facebox" id="facebox" style="display:none;">
  <div class="facebox-popup">
    <div class="facebox-content" role="dialog" aria-labelledby="facebox-header" aria-describedby="facebox-description">
    </div>
    <button type="button" class="facebox-close js-facebox-close" aria-label="Close modal">
      <svg class="octicon octicon-x" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.48 8l3.75 3.75-1.48 1.48L6 9.48l-3.75 3.75-1.48-1.48L4.52 8 .77 4.25l1.48-1.48L6 6.52l3.75-3.75 1.48 1.48L7.48 8z"/></svg>
    </button>
  </div>
</div>

  <template id="site-details-dialog">
  <details class="details-reset details-overlay details-overlay-dark lh-default text-gray-dark" open>
    <summary aria-haspopup="dialog" aria-label="Close dialog"></summary>
    <details-dialog class="Box Box--overlay d-flex flex-column anim-fade-in fast">
      <button class="Box-btn-octicon m-0 btn-octicon position-absolute right-0 top-0" type="button" aria-label="Close dialog" data-close-dialog>
        <svg class="octicon octicon-x" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.48 8l3.75 3.75-1.48 1.48L6 9.48l-3.75 3.75-1.48-1.48L4.52 8 .77 4.25l1.48-1.48L6 6.52l3.75-3.75 1.48 1.48L7.48 8z"/></svg>
      </button>
      <div class="octocat-spinner my-6 js-details-dialog-spinner"></div>
    </details-dialog>
  </details>
</template>

  <div class="Popover js-hovercard-content position-absolute" style="display: none; outline: none;" tabindex="0">
  <div class="Popover-message Popover-message--bottom-left Popover-message--large Box box-shadow-large" style="width:360px;">
  </div>
</div>

<div id="hovercard-aria-description" class="sr-only">
  Press h to open a hovercard with more details.
</div>


  </body>
</html>

