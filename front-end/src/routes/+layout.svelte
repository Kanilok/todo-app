<script>
    import "../app.css";
    import { logStore } from "./store.js"

    logStore.set({logged: false, username: "", admin: false})

    let is_logged = false;
    let username;
    let admin = false;
    logStore.subscribe(value => {
        is_logged = value.logged
        username = value.username
        admin = value.admin
    })

    function change(){
        document.getElementById("mobile-menu").classList.toggle("hidden");
    }

    function logOut(){
        localStorage.removeItem("access_token")
        logStore.set({logged: false, "username": "", admin: false})
        window.location.href = '/tasks';
    }
</script>

<nav class="bg-gray-800">
    <div class="mx-auto max-w-7xl px-2 sm:px-6 lg:px-8">
      <div class="relative flex h-16 items-center justify-between">
        <div class="absolute inset-y-0 left-0 flex items-center sm:hidden">
          <button type="button" on:click={change} class="inline-flex items-center justify-center rounded-md p-2 text-gray-400 hover:bg-gray-700 hover:text-white focus:outline-none focus:ring-2 focus:ring-inset focus:ring-white" aria-controls="mobile-menu" aria-expanded="false">
            <span class="sr-only">Open main menu</span>
            <svg class="block h-6 w-6" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" aria-hidden="true">
              <path stroke-linecap="round" stroke-linejoin="round" d="M3.75 6.75h16.5M3.75 12h16.5m-16.5 5.25h16.5" />
            </svg>
            <svg class="hidden h-6 w-6" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" aria-hidden="true">
              <path stroke-linecap="round" stroke-linejoin="round" d="M6 18L18 6M6 6l12 12" />
            </svg>
          </button>
        </div>
        <div class="flex flex-1 items-center justify-center sm:items-stretch sm:justify-start">
          <div class="flex flex-shrink-0 items-center">
            <p class="text-white">TODO-app</p>
          </div>
          <div class="hidden sm:ml-6 sm:block">
            <div class="flex space-x-4">
              <a href="/" class="text-gray-300 hover:bg-gray-700 hover:text-white rounded-md px-3 py-2 text-sm font-medium">Home</a>
              <a href="/tasks" class="text-gray-300 hover:bg-gray-700 hover:text-white rounded-md px-3 py-2 text-sm font-medium">Tasks</a>
              <a href="/about" class="text-gray-300 hover:bg-gray-700 hover:text-white rounded-md px-3 py-2 text-sm font-medium">About</a>
              {#if admin} 
                <a href="/users" class="text-gray-300 hover:bg-gray-700 hover:text-white rounded-md px-3 py-2 text-sm font-medium">Users</a>
              {/if}
            </div>
          </div>
        </div>
        <div class="absolute inset-y-0 right-0 flex items-center pr-2 sm:static sm:inset-auto sm:ml-6 sm:pr-0">
          {#if is_logged}
            <p class="text-gray-100 px-4">{username}</p>
            <button type="button" id="logout" on:click={logOut} class=" rounded border px-3 bg-gray-800 p-2 text-gray-100 hover:bg-white hover:text-gray-900">
                Log Out
            </button> 
          {:else}
            <a href="/login" id="login" class="rounded border px-3 bg-gray-800 p-2 text-gray-100 hover:bg-white hover:text-gray-900">
                Log In
            </a>
          {/if}
        </div>
      </div>
    </div>
  
    <div class="hidden" id="mobile-menu">
      <div class="space-y-1 px-2 pb-3 pt-2">
        <a href="/" class="text-gray-300 hover:bg-gray-700 hover:text-white block rounded-md px-3 py-2 text-base font-medium">Home</a>
        <a href="/tasks" class="text-gray-300 hover:bg-gray-700 hover:text-white block rounded-md px-3 py-2 text-base font-medium">Tasks</a>
        <a href="/about" class="text-gray-300 hover:bg-gray-700 hover:text-white block rounded-md px-3 py-2 text-base font-medium">About</a>
        {#if admin}
            <a href="/users" class="text-gray-300 hover:bg-gray-700 hover:text-white block rounded-md px-3 py-2 text-base font-medium">Users</a>
        {/if}
    </div>
    </div>
  </nav>

<slot></slot>

<footer class="bg-gray-800 text-center lg:text-left">
  <div class="p-3 text-center text-neutral-100">
    © 2023 Copyright:
    <span class="text-neutral-400">Kamil Motyl</span>
  </div>
</footer>  