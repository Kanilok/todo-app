import { writable } from 'svelte/store';

export const taskStore = writable();
export const logStore = writable();
export const editStore = writable();