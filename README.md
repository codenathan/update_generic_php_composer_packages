# Upgrading PHP Composer Packages

When doing upgrades of PHP versions you often also have to update your PHP Packages via composer. You would often spend ages trying to figure out which version is most comptible.

When i do upgrades often in my Laravel Projects. This is what i do :

- i first create a blank project called demo
- I update the composer file with the most basic required composer packages and ensure this installs via `composer update --with-all-dependencies`
- Create a git inital commit and run composer install if it hasn't been done 
- Copy  i copy any additional packages from my existing i have and paste it within require or require-dev. At the same time i replace the version of this composer package with a "*" For example

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

If this fails i repeat this process with a few packages and slowly increment whist still running the above composer command.

then i set the orginial version that has been installed back into the composer.json file by looking into the composer.lock file. To easily do this step run the python script found in this repository

If you are doing Laravel Upgrades of some old projects. Check out my comprehensive tutorial on [Upgrading from Laravel 5 to 8](https://codenathan.com/upgrading-from-laravel-5-to-laravel-8)
