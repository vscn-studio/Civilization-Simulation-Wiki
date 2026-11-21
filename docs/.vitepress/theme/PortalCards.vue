<script setup>
import { withBase } from 'vitepress'
defineProps({ items: { type: Array, required: true } })
</script>
<template><div class="portal-grid"><a v-for="item in items" :key="item.link" :href="withBase(item.link)" class="portal-card"><strong>{{ item.title }}</strong><span>{{ item.description }}</span></a></div></template>
