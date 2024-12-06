Once you have a google space channel you'd like these notifications to be sent to edit `/etc/sysconfig/google-chat-notifier` and set the
`NOTIFIER_CHAT_URL` environment variable to the webhook for the channel.

For any service that you'd like to have a notification about modify the service definition and add

```
[Unit]
...
OnFailure=google-chat-notifier@%n.service

```

This will send a failure message when if service fails.