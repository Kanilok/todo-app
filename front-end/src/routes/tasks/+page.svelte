<script>
    import { onMount } from 'svelte';
    import { taskStore } from "../store.js"
    import { logStore } from "../store.js"

    import Tasks from "./Tasks.svelte";
    
    let is_fetched = false;
    let verified = false;
    let logged_in =false;
    const SERWER_URL = "http://127.0.0.1:8000";

    async function fetchDataWithToken(token) {
        let tasks = [];
        await fetch(SERWER_URL + '/users/current', {
                headers: {
                    Authorization: `Bearer ${token}`,
                }
            }).then(response => {
                if(!response.ok){
                    throw new Error("You are not logged in")
                }
                return response.json()
            }).then(data => {
                verified = data.verified
                logged_in = true
                logStore.set({logged: true, username: data.username, admin: data.admin})
            }).catch(error => {
                console.error('Error fetching data:', error);
            });

        if(verified){
            await fetch(SERWER_URL + '/tasks', {
                headers: {
                    Authorization: `Bearer ${token}`,
                }
            }).then(response => {
                if(!response.ok){
                    console.log(response.status)
                    throw new Error("You are not logged in")
                }
                return response.json()
            }).then(data => {
                for(let i in data){
                tasks.push({id: data[i].id, 
                            task_name: data[i].task_name,
                            description: data[i].description,
                            is_done: data[i].is_done,
                            due_date: data[i].due_date,
                            done_date: data[i].done_date
                        })
                }
                is_fetched = true
                taskStore.set(tasks)
            }).catch(error => {
                console.error('Error fetching data:', error);
            });
        } 
    }

    onMount(() => {
        const token = localStorage.getItem("access_token")

        fetchDataWithToken(token);
    });
    
</script>

{#if is_fetched}
    <Tasks on:reFetch={() => (fetchDataWithToken(localStorage.getItem("access_token")))} {SERWER_URL}/>
{:else if logged_in}
    <h1 class="text-3xl p-2">You are not verified by admin</h1>
{:else}
    <h1 class="text-3xl p-2">You are not logged in</h1>
{/if}
