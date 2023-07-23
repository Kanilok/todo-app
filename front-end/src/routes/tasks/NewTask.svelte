<script>
    import { createEventDispatcher } from "svelte";

    let description
    let date

    const dispatch = createEventDispatcher();

    function onSubmit(){
        dispatch("onSubmit", {description:description, date:date})
    }
</script>

<form on:submit|preventDefault={onSubmit}>
    <div style="margin:8px">
        <input  bind:value={description} type="text" class="appearance-none border rounded w-full py-2 px-2 text-gray-700" placeholder="Task description..." style="width:250px; display:inline-block">
         due:
        <input bind:value={date} type="date" class="appearance-none border rounded w-full py-2 px-2 text-gray-700" style="width:180px; display:inline-block">
        <button class="hover:bg-blue-700 text-blue-700 font-semibold hover:text-white py-2 px-4 border border-blue-700 rounded" action="submit">add new task</button>
    </div>
</form>

<style>
    
</style>
