import firebase from "firebase";

import { ref, onUnmounted } from "vue";

import moment from 'moment';

/* code from our Firebase console */
const config = {
  apiKey: import.meta.env.VITE_FIREBASE_API_KEY,
  authDomain: import.meta.env.VITE_FIREBASE_AUTH_DOMAIN,
  projectId: "honameulo",
  storageBucket: import.meta.env.VITE_FIREBASE_STORAGE_BUCKET,
  messagingSenderId: import.meta.env.VITE_FIREBASE_MESSAGEING_SENDER_ID,
  appId: import.meta.env.VITE_FIREBASE_APP_ID,
};

// Initialize Firebase
const firebaseApp = firebase.initializeApp(config);

const db = firebaseApp.firestore();

const usersCollection = db.collection("users");
const personalProgramsCollection = db.collection("personal-programs");
const localCommunityProgramsCollection = db.collection(
  "local-community-programs"
);

/*
 * users collection handling
 */
export const createUser = (user: any) => {
  return usersCollection.add(user);
};

export const getUser = async (id: string) => {
  const user = await usersCollection.doc(id).get();
  return user.exists ? user.data() : null;
};

export const updateUser = (id: string, user: any) => {
  return usersCollection.doc(id).update(user);
};

export const deleteUser = (id: string) => {
  return usersCollection.doc(id).delete();
};

export const useLoadUsers = () => {
  const users = ref({});
  const close = usersCollection.onSnapshot((snapshot) => {
    users.value = snapshot.docs.map((doc) => ({ id: doc.id, ...doc.data }));
  });
  onUnmounted(close);

  return users;
};

/*
 * personal-programs collection handling
 */
export const createPersonalProgram = (program: any) => {
  return personalProgramsCollection.add(program);
};

export const getPersonalProgram = async (id: string) => {
  const program = await personalProgramsCollection.doc(id).get();
  return program.exists ? program.data() : null;
};

export const getAllPersonalProgram = async () => {
  const program = await personalProgramsCollection.get();
  return program.empty
    ? []
    : program.docs.map((doc) => {
        return { id: doc.id, ...doc.data() };
      });
};

export const updatePersonalProgram = (id: string, program: any) => {
  return personalProgramsCollection.doc(id).update(program);
};

export const deletePersonalProgram = (id: string) => {
  return personalProgramsCollection.doc(id).delete();
};

/*
 * local-community-programs collection handling
 */
export const createLocalCommunityProgram = (program: any) => {
  return localCommunityProgramsCollection.add(program);
};

export const getLocalCommunityProgram = async (id: string) => {
  const program = await localCommunityProgramsCollection.doc(id).get();
  return program.exists ? program.data() : null;
};

export const getAllLocalCommunityProgram = async () => {
  const program = await localCommunityProgramsCollection.get();
  return program.empty
    ? []
    : program.docs.map((doc) => {
        return { id: doc.id, ...doc.data() };
      });
};

export const updateLocalCommunityProgram = (id: string, program: any) => {
  return localCommunityProgramsCollection.doc(id).update(program);
};

export const deleteLocalCommunityProgram = (id: string) => {
  return localCommunityProgramsCollection.doc(id).delete();
};

/*
 * utility methods
 */ 
export const getTimestamp = (date: any, format: string) =>
  firebase.firestore.Timestamp.fromDate(moment(date, format).toDate());
