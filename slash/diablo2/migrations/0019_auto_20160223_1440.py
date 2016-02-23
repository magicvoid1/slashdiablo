# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-23 14:40
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('diablo2', '0018_report_depth'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='account',
            options={'permissions': (('account_sync', 'Can resync Diablo 2 accounts'), ('account_sync_all', 'Can resync all Diablo 2 accounts at once'), ('character_sync', 'Can resync Diablo 2 characters'), ('character_sync_all', 'Can resync all Diablo 2 characters at once'), ('moderation_enabled', 'Can access moderation tools'), ('log_sync', 'Can sync the gameserver logs'), ('log_parse', 'Can parse the gameserver logs'), ('moderation_investigate', 'Can access the investigate section'), ('moderation_action', 'Can access the actions section'), ('moderation_gamelist', 'Can access the game info section'), ('moderation_history', 'Can access the history section'), ('moderation_system', 'Can access the system secton'), ('moderation_investigate_database', 'Can investigate using the database'), ('moderation_investigate_database_password', 'Can investigate using the database and lookup matching passwords'), ('moderation_investigate_logs', 'Can investigate using the logs'), ('moderation_investigate_report', 'Can generate reports'), ('moderation_investigate_account', 'Can investigate via account model '), ('moderation_investigate_character', 'Can investigate via character model'), ('moderation_action_lock', 'Can preform account lock'), ('moderation_action_unlock', 'Can preform account unlock'), ('moderation_action_ban', 'Can preform ip ban'), ('moderation_action_unban', 'Can preform ip unban'), ('moderation_action_kick', 'Can preform kick'), ('moderation_action_announce', 'Can preform announcement'), ('moderation_action_chpass', 'Can preform password change'), ('moderation_history_gs', 'Can view history for gameserver'), ('moderation_history_report', 'Can view history for reports'), ('moderation_history_lookup', 'Can view history for lookups'), ('moderation_history_lookup_all', 'Can view history for lookups by everyone'), ('moderation_history_action', 'Can view history for actions'), ('moderation_history_action_all', 'Can view history for actions by everyone'), ('moderation_system_pvpgn_start', 'Can manage pvpgn and start processes'), ('moderation_system_pvpgn_stop', 'Can manage pvpgn and stop processes'), ('moderation_system_pvpgn_restart', 'Can manage pvpgn and restart processes'), ('moderation_system_d2gs_start', 'Can manage d2gs and start processes'), ('moderation_system_d2gs_stop', 'Can manage d2gs and stop processes'), ('moderation_system_d2gs_restart', 'Can manage d2gs and restart processes'), ('moderation_system_status', 'Can view system status'), ('moderation_gamelist_list', 'Can view gamelist'), ('moderation_gamelist_detail', 'Can view game details'), ('moderation_passwords', 'Can view various passwords'), ('moderation_passwords_discord', 'Can view discord password'), ('moderation_passwords_subreddit', 'Can view subreddit password'), ('moderation_passwords_telnet', 'Can view telnet password'), ('moderation_passwords_game', 'Can view in game moderator password')), 'verbose_name': 'Account'},
        ),
    ]
