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
    <div class="grid gap-6 mb-6 md:grid-cols-2">
        <div>
            <label for="task_name" class="block mb-2 text-sm font-medium text-gray-900">Task name</label>
            <input bind:value={description} type="text" id="task_name" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 " placeholder="laundry" required>
        </div>
        <div>
            <label for="due_date" class="block mb-2 text-sm font-medium text-gray-900 ">Due date <span class="text-gray-500"> (optional) </span></label>
            <input  bind:value={date} type="date" id="due_date" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5" >
        </div>
    </div> 
    <div class="mb-6">
        <label for="task_description" class="block mb-2 text-sm font-medium text-gray-900 ">Task description <span class="text-gray-500"> (optional) </span></label>
        <input type="text" id="task_description" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 " placeholder="Do all the laundry and later iron it">
    </div> 
    
    <button type="submit" class="hover:bg-blue-700 text-blue-700 font-semibold hover:text-white py-2 px-4 border border-blue-700 rounded">Add new task</button>
</form>

