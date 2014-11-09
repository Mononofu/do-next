# do-next
Simple commandline utility to make choosing the next task to work on as painless as possible.

```
$ python do-next.py
80 WaniKani reviews
```

Supports reading from multiple sources of tasks, currently:
- available [WaniKani](https://www.wanikani.com) reviews and lessons
- pending [Duolingo](https://www.duolingo.com/) streaks
- [PlainTasks](https://www.duolingo.com/) marked with a predefined @tag

Sources are split in two groups, mandatory and optional. If any of the sources in the mandatory group returns a task, that task will be printed by the script, in the order the sources are listed.

If no mandatory source returns a task, a randomly selected task from the optional group is printed.
