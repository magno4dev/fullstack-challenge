<template>
    <Login v-if="$route.path === '/login'" />
    <Error v-else-if="$route.path === '/error'" />
    <Access v-else-if="$route.path === '/access'" />
    <NotFound v-else-if="$route.path === '/notfound'" />
    <App :theme="theme" :layout="layout" @theme-change="onThemeChange" @layout-change="onLayoutChange" v-else />
</template>

<script>
    import App from './App.vue';

	export default {
        data() {
            return {
                theme: 'blue',
                layout: 'layout-blue'
            }
        },
        methods: {
            onThemeChange(theme) {
                this.theme = theme;
            },
            onLayoutChange(layout) {
                this.layout = layout;
            }
        },
        components: {
            "App": App
        }
	}
</script>

<style scoped>
</style>
