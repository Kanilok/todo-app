<script>
    import { createEventDispatcher } from "svelte";

    let task_name
    let description
    let date

    const dispatch = createEventDispatcher();

    function onSubmit(){
        if(date == ""){
            date = undefined
        }
        if(description == ""){
            description = undefined
        }
        dispatch("onSubmit", {task_name:task_name, date:date, description:description})
    }
</script>


<form on:submit|preventDefault={onSubmit}>
    <div class="grid gap-6 mb-6 md:grid-cols-2">
        <div>
            <label for="task_name" class="block mb-2 text-sm font-medium text-gray-900">Task name<span class="text-red-500"> * </span></label>
            <input bind:value={task_name} type="text" id="task_name" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 " placeholder="laundry" required>
        </div>
        <div>
            <label for="due_date" class="block mb-2 text-sm font-medium text-gray-900 ">Due date</label>
            <input bind:value={date} type="date" id="due_date" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5" >
        </div>
    </div> 
    <div class="mb-6">
        <label for="task_description" class="block mb-2 text-sm font-medium text-gray-900 ">Task description</label>
        <textarea bind:value={description} id="task_descripion" rows="3" class="block p-2 w-full text-sm text-gray-900 bg-gray-50 rounded-lg border border-gray-300 focus:ring-blue-500 focus:border-blue-500 " placeholder="Write task description here..."></textarea>
    </div> 
    
    <button type="submit" class="hover:bg-blue-700 text-blue-700 font-semibold hover:text-white py-2 px-4 border border-blue-700 rounded">Add new task</button>
</form>

