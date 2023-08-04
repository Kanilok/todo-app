<script>
    export let id
    export let username
    export let verified
    export let SERWER_URL

    function verify(){
        verified = !verified
        fetch(SERWER_URL + "/users/" + id,{
            method: 'PUT',
        })
    }
</script>

<tr class="bg-gray-100 border-b  hover:bg-gray-50 ">
    <th class="w-64 px-6 py-4 font-medium text-gray-900 whitespace-nowrap cursor-pointer">
        {username} 
    </th>
    <th class="px-6 py-4 font-medium text-gray-900 whitespace-nowrap cursor-pointer">
        {#if verified}
            <p class="text-green-600">Verified</p> 
        {:else}
            <p class="text-red-600">Not verified</p> 
        {/if}
    </th>
    <td class=" py-4 text-center">
        <button class="hover:bg-blue-600 text-blue-600 font-semibold hover:text-white py-2 px-4 border border-blue-600 rounded" type="button" on:click={verify}>Toggle verify</button>
    </td>
</tr>