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
    from metabaseapi.cli.commands import ee_action_v2 as ee_action_v2
    from metabaseapi.cli.commands import ee_advanced_permissions as ee_advanced_permissions
    from metabaseapi.cli.commands import ee_ai_controls as ee_ai_controls
    from metabaseapi.cli.commands import eid_translation as eid_translation
    from metabaseapi.cli.commands import email as email
    from metabaseapi.cli.commands import embed as embed
    from metabaseapi.cli.commands import embed_theme as embed_theme
    from metabaseapi.cli.commands import field as field
    from metabaseapi.cli.commands import frontend_errors as frontend_errors
    from metabaseapi.cli.commands import geojson as geojson
    from metabaseapi.cli.commands import glossary as glossary
    from metabaseapi.cli.commands import google as google
    from metabaseapi.cli.commands import ldap as ldap
    from metabaseapi.cli.commands import llm as llm
    from metabaseapi.cli.commands import logger as logger
    from metabaseapi.cli.commands import login_history as login_history
    from metabaseapi.cli.commands import measure as measure
    from metabaseapi.cli.commands import metabot as metabot
    from metabaseapi.cli.commands import metric as metric
    from metabaseapi.cli.commands import model_index as model_index
    from metabaseapi.cli.commands import moderation_review as moderation_review
    from metabaseapi.cli.commands import native_query_snippet as native_query_snippet
    from metabaseapi.cli.commands import notification as notification
    from metabaseapi.cli.commands import notify as notify
    from metabaseapi.cli.commands import permissions as permissions
    from metabaseapi.cli.commands import persist as persist
    from metabaseapi.cli.commands import premium_features as premium_features
    from metabaseapi.cli.commands import preview_embed as preview_embed
    from metabaseapi.cli.commands import product_feedback as product_feedback
    from metabaseapi.cli.commands import public as public
    from metabaseapi.cli.commands import pulse as pulse
    from metabaseapi.cli.commands import revision as revision
    from metabaseapi.cli.commands import search as search
    from metabaseapi.cli.commands import segment as segment
    from metabaseapi.cli.commands import session as session
    from metabaseapi.cli.commands import setting as setting
    from metabaseapi.cli.commands import setup as setup
    from metabaseapi.cli.commands import slack as slack
    from metabaseapi.cli.commands import table as table
    from metabaseapi.cli.commands import task as task
    from metabaseapi.cli.commands import tiles as tiles
    from metabaseapi.cli.commands import timeline as timeline
    from metabaseapi.cli.commands import timeline_event as timeline_event
    from metabaseapi.cli.commands import transform as transform
    from metabaseapi.cli.commands import transform_job as transform_job
    from metabaseapi.cli.commands import transform_tag as transform_tag
    from metabaseapi.cli.commands import upload as upload
    from metabaseapi.cli.commands import user as user
    from metabaseapi.cli.commands import user_key_value as user_key_value
    from metabaseapi.cli.commands import util as util

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
        ee_action_v2,
        ee_advanced_permissions,
        ee_ai_controls,
        eid_translation,
        email,
        embed,
        embed_theme,
        field,
        frontend_errors,
        geojson,
        glossary,
        google,
        ldap,
        llm,
        logger,
        login_history,
        measure,
        metabot,
        metric,
        model_index,
        moderation_review,
        native_query_snippet,
        notification,
        notify,
        permissions,
        persist,
        premium_features,
        preview_embed,
        product_feedback,
        public,
        pulse,
        revision,
        search,
        segment,
        session,
        setting,
        setup,
        slack,
        table,
        task,
        tiles,
        timeline,
        timeline_event,
        transform,
        transform_job,
        transform_tag,
        upload,
        util,
        user,
        user_key_value,
    )


__all__: list[str] = []
