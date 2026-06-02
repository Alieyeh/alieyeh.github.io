---
title: "PlantBuddy Cross-Platform Plant Marketplace"
collection: portfolio
category: software
permalink: /software/plantbuddy/
excerpt: "Cross-platform Expo and Supabase application for plant profiles, peer-to-peer listings, sitter applications, swaps and structured handoffs."
---

## Overview

PlantBuddy is a personal full-stack product and engineering project for a plant-native marketplace and care network.

The current build supports the core idea that plants are not just generic marketplace items. Each plant has its own profile, care context and lifecycle, then can be listed for sitting, gifting, sale or exchange through one shared platform.

## Current Implementation

- Active cross-platform app in Expo and React Native, targeting web, Android and iOS
- Supabase backend using Auth, PostgreSQL, PostgREST APIs and Row Level Security
- Plant profile management with care fields, age/life-stage options and editable care autofill from common plant care profiles
- Listing flows for sitting requests, gifts and sales, with browsing, search, filtering and sort logic
- Sitter application review, swap proposal handling, handoff confirmation and review-oriented exchange flows
- Shared design tokens, navigation structure and app-level configuration handling for missing Supabase environment variables
- Node-based unit, integration and smoke tests covering form logic, listing helpers, browsing, exchange inbox composition and project wiring

## What It Demonstrates

- Cross-platform mobile and web application architecture
- Product thinking around trust, care context and peer-to-peer exchange
- Direct-to-Supabase frontend design with database-enforced authorization
- PostgreSQL schema modelling with enums, constraints, indexes, ownership rules and RLS policies
- Clean separation of screens, services, domain helpers, utilities and tests
- Pragmatic migration from an earlier native Android/REST concept to a simpler, more deployable Supabase architecture

## Earlier Android Work

The repository also keeps an older Java Android implementation and database diagrams as reference material. The active direction has moved to the Expo/Supabase app, while the Android folder still documents useful work on mobile architecture, Retrofit-style API integration, encrypted session storage, UML and ER modelling.

## Repository

GitHub repository: [github.com/Alieyeh/PlantBuddy](https://github.com/Alieyeh/PlantBuddy)

**Tags:** React Native, Expo, Supabase, PostgreSQL, Row Level Security, JavaScript, mobile development, product design, software testing, Android, Java
