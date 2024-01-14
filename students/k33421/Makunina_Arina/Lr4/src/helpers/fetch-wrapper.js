import { useAuthStore } from '@/stores';

export const fetchWrapper = {
  get: request('GET'),
  post: request('POST'),
  put: request('PUT'),
  delete: request('DELETE')
};

const logout = async () => {
  try {
    const authStore = useAuthStore();

    await fetchWrapper.post('/auth/logout/');

    authStore.logout();
    router.push('/login');
  } catch (error) {
    console.error("Error during logout:", error);
  }
}

function request(method) {
  return async (url, body, query) => {
    const headers = await authHeader(url);
    const requestOptions = {
      method,
      headers,
    };
    if (body) {
      requestOptions.headers['Content-Type'] = 'application/json';
      requestOptions.body = JSON.stringify(body);
    }
    if (query) {
      url = url + "?" + new URLSearchParams(query)
    }
    return fetch(url, requestOptions).then(handleResponse);
  }
}

async function authHeader(url) {
  const authStore = useAuthStore();
  const isLoggedIn = !!authStore.access;
  const isApiUrl = url.startsWith(import.meta.env.VITE_API_URL);

  if (isLoggedIn && isApiUrl) {
    return { Authorization: `Bearer ${authStore.access}` };
  } else {
    return {};
  }
}

async function handleResponse(response) {
  return response.text().then(async text => {
    let data;

    const contentType = response.headers.get('Content-Type');

    if (contentType && contentType.includes('application/json')) {
      data = JSON.parse(text);
    } else {
      data = text;
    }

    if (!response.ok) {
      const authStore = useAuthStore();
      if ([401, 403].includes(response.status) && authStore.access) {
        await authStore.logout();
      }

      const error = new Error(response.statusText);
      error.status = response.status;
      error.data = data;
      throw error;
    }

    return data;
  });
}
