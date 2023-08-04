<script>
    import User from "./User.svelte"

    export let users
    export let SERWER_URL
</script>

<div class="m-8 relative overflow-x-auto shadow-md sm:rounded-lg">
    <table class="w-full text-sm text-left text-gray-500">
      <thead class="text-xs text-gray-700 uppercase bg-gray-300">
          <tr>
              <th scope="col" class="w-64 px-6 py-3">
                Username
              </th>
              <th scope="col" class="px-6 py-3">
                Verified
              </th>
              <th scope="col" class="px-6 py-3">
                <span class="sr-only">Verify</span>
              </th>
          </tr>
      </thead>
      <tbody>
      {#each users as {username, verified, id}}
          <User {username} {id} {verified} {SERWER_URL}/>
      {/each}
      </tbody>
    </table>
  </div>