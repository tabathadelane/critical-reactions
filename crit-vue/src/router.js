import Vue from "vue";
import Router from "vue-router";
import Home from "./views/Home.vue";
import Blog from "./views/Blog.vue";
import Book from "./views/Book.vue";
import Members from "./views/Members.vue";
import Party from "./views/Party.vue";
import Testimonials from "./views/Testimonials.vue";

Vue.use(Router);

export default new Router({
  routes: [
    {
        path: "/",
        name: "home",
        component: Home
    },
    {
        path: "/party",
        name: "party",
        component: Party
    },
    {
        path: "/members",
        name: "members",
        component: Members
    },
    {
        path: "/testimonials",
        name: "tesimonials",
        component: Testimonials
    },
    {
        path: "/bookus",
        name: "book",
        component: Book
    },
    {
        path: "/AltheasBardBlog",
        name: "blog",
        component: Blog
    },
    {
        path: "*",
        redirect: '/'
    }

  ]
});