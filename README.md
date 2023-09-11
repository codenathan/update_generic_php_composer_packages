# Upgrading PHP Composer Packages

When doing upgrades of PHP versions you often also have to update your PHP Packages via composer. You would often spend ages trying to figure out which version is most comptible.

When i do upgrades often in my Laravel Projects. This is what i do :

- i first create a blank project called demo
- I update the composer file with the most basic required composer packages and ensure this installs via `composer update --with-all-dependencies`
- Create a git inital commit and run composer install if it hasn't been done 
- Copy  i copy any additional packages from my existing `composer.json` i have and paste it within my demo projects `composer.json` require or require-dev section. At the same time i replace the version of this composer package with a "*" For example

```
  "barryvdh/laravel-dompdf": "*",
  "barryvdh/laravel-ide-helper": "*",
  "friendsofphp/php-cs-fixer": "*",
  "maatwebsite/excel": "*",
  "owen-it/laravel-auditing": "*",
  "plank/laravel-mediable": "*",
  "spatie/laravel-analytics": "*",
  "spatie/laravel-failed-job-monitor": "*",
  "spatie/laravel-permission": "*",
  "spatie/laravel-responsecache": "*",
  "tightenco/ziggy": "*",
  "tucker-eric/eloquentfilter": "*"
```

Then i just let composer do its magic and run `composer update --with-all-dependencies` 

If this fails i repeat this process with a few packages and slowly increment whist still running the above composer command. During each step this works replace the "*" from the above `composer.json` file with the actual version that has been installed by looking at the `composer.lock` file, to make your life easier during this step simply run the python script found within this repo. Ensure you do a git commit each time a package installation works if you are doing slow increments and have lots of packages. Sometimes if this errors out a lot simply delete the composer.lock and vendor folder and try again within the demo project since you will delete this project after you are done anyway

Once i have a fully working version of a `composer.json` file, i copy it back from my demo project back into my original project and run `composer.json`

If you are doing Laravel Upgrades of some old projects. Check out my comprehensive tutorial on [Upgrading from Laravel 5 to 8](https://codenathan.com/upgrading-from-laravel-5-to-laravel-8)
