<script>
    import { onMount } from 'svelte';
    import Tasks from "./Tasks.svelte";
    
    export let is_fetched = false
    let tasks = [];

    async function fetchDataWithToken(token) {
        await fetch('http://127.0.0.1:8000/tasks', {
                headers: {
                Authorization: `Bearer ${token}`,
                }
            }).then(response => {
                if(!response.ok){
                    throw new Error("You are not logged in")
                }
                return response.json()
            }).then(data => {
                for(let i in data){
                tasks.push({id: data[i].id, 
                            task_name: data[i].task_name,
                            is_done: data[i].is_done,
                            due_date: data[i].due_date,
                            done_date: data[i].done_date
                        })
                }
                is_fetched = true
            }).catch(error => {
                console.error('Error fetching data:', error);
            });
    }

    onMount(() => {
        const token = localStorage.getItem("access_token")

        fetchDataWithToken(token);
    });
    
</script>

{#if is_fetched}
    <Tasks on:reFetch={() => (fetchDataWithToken(localStorage.getItem("access_token")))} {tasks}/>
{:else}
    <h1 class="text-3xl p-2">You are not logged in</h1>
{/if}
