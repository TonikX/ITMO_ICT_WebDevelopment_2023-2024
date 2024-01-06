import { createRouter, createWebHistory } from 'vue-router'
import { useAuthStore } from '@/stores';
import { LoginComponent, RegisterComponent, ScheduleComponent } from "@/components";
import { DispatcherHome, SubDeanHome, TeachersList, Unauth, GroupList } from "@/views";

const routes = [
  { path: '/login', component: LoginComponent },
  { path: '/register', component: RegisterComponent },
  { path: '/unauth',
    name: 'Unauth',
    component: Unauth,
  },
  {
    path: '/',
    component: function () {
      const auth = useAuthStore();

      if (auth.role === "Заместитель декана") {
        return SubDeanHome;
      } else if (auth.role === "Диспетчер") {
        return DispatcherHome;
      } else {
        return Unauth;
      }
    },
  },
  {
    path: '/teachers',
    component: function () {
      const auth = useAuthStore();

      if (auth.role === "Заместитель декана") {
        return TeachersList;
      } else if (auth.role === "Диспетчер") {
        return Unauth;
      } else {
        return Unauth;
      }
    },
  },
    {
    path: '/groups',
    component: function () {
      const auth = useAuthStore();

      if (auth.role === "Заместитель декана") {
        return GroupList;
      } else if (auth.role === "Диспетчер") {
        return Unauth;
      } else {
        return Unauth;
      }
    },
  },
  {
    path: '/schedule',
    component: ScheduleComponent,
    props: route => ({
      group: route.query.group,
      semester: route.query.semester,
    }),
  },
];

export const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes,
});

router.beforeEach(async (to, from, next) => {
  const publicPages = ['/login', '/register'];
  const authRequired = !publicPages.includes(to.path);
  const authStore = useAuthStore();

  if (authStore.access) {
    await authStore.update_role();
  }

  if (to.path === '/schedule' && authStore.role !== 'Диспетчер') {
    return next({ path: '/unauth' });
  }

  if (authStore.access && (to.path.startsWith('/login') || to.path.startsWith('/register'))) {
    return next({ path: '/' });
  }

  if (authRequired && !authStore.access) {
    authStore.returnUrl = to.fullPath;
    return next({ path: '/login' });
  }

  next();
});
