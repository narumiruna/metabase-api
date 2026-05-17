from __future__ import annotations


def _register_commands() -> None:
    from metabaseapi.cli.commands import action as action
    from metabaseapi.cli.commands import activity as activity
    from metabaseapi.cli.commands import agent as agent
    from metabaseapi.cli.commands import ai_entity_analysis as ai_entity_analysis
    from metabaseapi.cli.commands import alert as alert
    from metabaseapi.cli.commands import analytics as analytics
    from metabaseapi.cli.commands import api_key as api_key
    from metabaseapi.cli.commands import automagic as automagic
    from metabaseapi.cli.commands import bookmark as bookmark
    from metabaseapi.cli.commands import bug_reporting as bug_reporting
    from metabaseapi.cli.commands import cache as cache
    from metabaseapi.cli.commands import card as card
    from metabaseapi.cli.commands import card_query as card_query
    from metabaseapi.cli.commands import channel as channel
    from metabaseapi.cli.commands import cloud_migration as cloud_migration
    from metabaseapi.cli.commands import collection as collection
    from metabaseapi.cli.commands import collection_graph as collection_graph
    from metabaseapi.cli.commands import collection_root as collection_root
    from metabaseapi.cli.commands import comment as comment
    from metabaseapi.cli.commands import dashboard as dashboard
    from metabaseapi.cli.commands import dashboard_query as dashboard_query
    from metabaseapi.cli.commands import data_studio as data_studio
    from metabaseapi.cli.commands import database as database
    from metabaseapi.cli.commands import dataset as dataset
    from metabaseapi.cli.commands import document as document
    from metabaseapi.cli.commands import email as email
    from metabaseapi.cli.commands import embed as embed
    from metabaseapi.cli.commands import field as field
    from metabaseapi.cli.commands import public as public
    from metabaseapi.cli.commands import table as table
    from metabaseapi.cli.commands import user as user
    from metabaseapi.cli.commands import user_key_value as user_key_value

    _ = (
        action,
        activity,
        agent,
        ai_entity_analysis,
        alert,
        analytics,
        api_key,
        automagic,
        bookmark,
        bug_reporting,
        cache,
        card,
        card_query,
        channel,
        cloud_migration,
        collection,
        collection_graph,
        collection_root,
        comment,
        dashboard,
        dashboard_query,
        data_studio,
        database,
        dataset,
        document,
        email,
        embed,
        field,
        public,
        table,
        user,
        user_key_value,
    )


__all__: list[str] = []
