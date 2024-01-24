<script setup lang="ts">
import Toaster from '@/components/ui/toast/Toaster.vue'
import * as z from 'zod'

import {useForm} from 'vee-validate'
import {toTypedSchema} from '@vee-validate/zod'
import { useToast } from '@/components/ui/toast/use-toast'

import {vAutoAnimate} from '@formkit/auto-animate'
import {Button} from '@/components/ui/button'
import {FormControl, FormField, FormItem, FormLabel, FormMessage,} from '@/components/ui/form'
import {Input} from '@/components/ui/input'
import {Card, CardContent, CardDescription, CardFooter, CardHeader, CardTitle,} from '@/components/ui/card'
import {
  Tabs,
  TabsContent,
  TabsList,
  TabsTrigger,
} from '@/components/ui/tabs'

const { toast } = useToast()

interface User {
  username: string;
  password: string;
  ntfy_channel: string;
  data?: object;
}

const formSchema = toTypedSchema(z.object({
  username: z.string().length(9).startsWith("s"),
  password: z.string()
}))

const {handleSubmit} = useForm({
  validationSchema: formSchema,
})

const authData = ref<User | null>(null)
const authRegistrationSuccessful = ref<boolean>(false)
const authDeletionSuccessful = ref<boolean>(false)

const onSubmitRegistration = handleSubmit(async (values) => {
  const {data} = await useFetch<User>('/submit', {
    query: {username: values.username, password: values.password},
    method: "POST",
  })
  console.log(data.value)
  if (data.value) {
    if (!data.value.ntfy_channel) {
      authRegistrationSuccessful.value = false
      toast({
        variant: "destructive",
        title: 'Authentication Error',
        description: 'Username/Password Incorrect',
      });
    } else {
      authData.value = data.value
      authRegistrationSuccessful.value = true
    }
  } else {
    authRegistrationSuccessful.value = false
    toast({
      variant: "destructive",
      title: 'Authentication Error',
      description: 'Username/Password Incorrect',
    });
  }
})

const onSubmitDeletion = handleSubmit(async (values) => {
  const {data} = await useFetch<User>('/submit', {
    query: {username: values.username, password: values.password},
    method: "DELETE",
  })
  console.log(data.value)
  if (data.value) {
    if (!data.value.ntfy_channel) {
      authDeletionSuccessful.value = false
      toast({
        variant: "destructive",
        title: 'Authentication Error',
        description: 'Username/Password Incorrect',
      });
    } else {
      authData.value = data.value
      authDeletionSuccessful.value = true
    }
  } else {
    authDeletionSuccessful.value = false
    toast({
      variant: "destructive",
      title: 'Authentication Error',
      description: 'Username/Password Incorrect',
    });
  }
})

</script>

<template>
  <div class="border-b px-4 fixed top-0 w-full z-10 backdrop-blur-3xl">
    <div class="flex h-16 items-center">
      <NuxtLink to="/" class="flex items-center">
        <Icon name="mdi:skull-crossbones" />
        <h1 class="font-black">TSIMS Notify</h1>
      </NuxtLink>

      <div class="ml-auto flex items-center space-x-4" >
        <NuxtLink to="https://github.com/qwerzl/notify.tsims.lol" class="flex items-center">
          <Icon name="mdi:github" size="1.5em"/>
        </NuxtLink>
      </div>
    </div>
  </div>

  <div class="max-w-[96ch] px-6 mx-auto mt-6 relative top-16">
    <Tabs default-value="register">
      <TabsList class="grid grid-cols-2 w-[400px]">
        <TabsTrigger value="register">
          Register
        </TabsTrigger>
        <TabsTrigger value="delete">
          Stop Notification
        </TabsTrigger>
      </TabsList>
      <TabsContent value="register" class="mt-5">
        <div class="rounded border border-accent">
          <form class="space-y-6 m-6" @submit="onSubmitRegistration">
            <div class="text-xl">
              <div class="font-bold">
                Register/Update your password
              </div>
              <div class="text-gray-500 text-[0.95rem]">
                Type in your TSIMS credentials here to start receiving notifications.
              </div>
            </div>
            <FormField v-slot="{ componentField }" name="username">
              <FormItem v-auto-animate>
                <FormLabel>Username</FormLabel>
                <FormControl>
                  <Input type="text" placeholder="Your username in TSIMS" v-bind="componentField"/>
                </FormControl>
                <FormMessage>no</FormMessage>
              </FormItem>
            </FormField>

            <FormField v-slot="{ componentField }" name="password">
              <FormItem v-auto-animate>
                <FormLabel>Password</FormLabel>
                <FormControl>
                  <Input type="password" placeholder="Your password in TSIMS" v-bind="componentField"/>
                </FormControl>
                <FormMessage/>
              </FormItem>
            </FormField>

            <Button type="submit">
              Submit
            </Button>
          </Form>
        </div>
          <Card class="shadow-none mt-6" v-auto-animate v-if="authRegistrationSuccessful">
            <CardHeader>
              <CardTitle>Authentication Successful!</CardTitle>
              <CardDescription>Follow the steps below to start receiving messages.</CardDescription>
            </CardHeader>
            <CardContent class="grid gap-4">
              <div>
                <div
                    class="mb-4 grid grid-cols-[25px_1fr] items-start pb-4 last:mb-0 last:pb-0"
                >
                  <span class="flex h-2 w-2 translate-y-1 rounded-full bg-sky-500"/>
                  <div class="space-y-1">
                    <p class="text-sm font-medium leading-none">
                      1. Download ntfy.sh app for your device
                    </p>
                    <p class="text-sm text-muted-foreground">
                      If you haven't done so, refer to
                      <NuxtLink to="https://ntfy.sh/" class="text-sky-500 hover:underline">ntfy.sh</NuxtLink>
                      or start with
                      <NuxtLink to="https://ntfy.tsims.lol" class="text-sky-500 hover:underline">our webapp</NuxtLink>
                      .
                    </p>
                  </div>
                </div>

                <div
                    class="mb-4 grid grid-cols-[25px_1fr] items-start pb-4 last:mb-0 last:pb-0"
                >
                  <span class="flex h-2 w-2 translate-y-1 rounded-full bg-sky-500"/>
                  <div class="space-y-1">
                    <p class="text-sm font-medium leading-none">
                      2. Subscribe to your notification channel
                    </p>
                    <div class="text-sm text-muted-foreground">
                      Click "Subscribe to topic" button and enter the following for topic name:
                      <div class="mt-1 rounded border-accent border-2 px-3 py-1 font-mono" v-if="authData">
                        {{ authData.ntfy_channel }}
                      </div>
                      <div class="mt-1">
                        Then click "use another server", enter the following for server URL:
                      </div>
                      <div class="mt-1 rounded border-accent border-2 px-3 py-1 font-mono">
                        https://ntfy.tsims.lol
                      </div>
                      <div class="mt-1">
                        Then click "Subscribe".
                      </div>
                    </div>
                  </div>
                </div>

                <div
                    class="mb-4 grid grid-cols-[25px_1fr] items-start pb-4 last:mb-0 last:pb-0"
                >
                  <span class="flex h-2 w-2 translate-y-1 rounded-full bg-sky-500"/>
                  <div class="space-y-1">
                    <p class="text-sm font-medium leading-none">
                      3. Wait for the first message
                    </p>
                    <div class="text-sm text-muted-foreground">
                      You should receive a notification within 6 minutes. Then you're good to go. <br />
                      Note that topic name changes everytime you log in on this website.
                    </div>
                  </div>
                </div>

              </div>
            </CardContent>
          </Card>
      </TabsContent>

      <TabsContent value="delete" class="mt-5">
        <div class="rounded border border-accent">
          <form class="space-y-6 m-6" @submit="onSubmitDeletion">

            <div class="text-xl">
              <div class="font-bold">
                Stop notification
              </div>
              <div class="text-gray-500 text-[0.95rem]">
                Type in your TSIMS credentials here to stop receiving notifications.
              </div>
            </div>

            <FormField v-slot="{ componentField }" name="username">
              <FormItem v-auto-animate>
                <FormLabel>Username</FormLabel>
                <FormControl>
                  <Input type="text" placeholder="Your username in TSIMS" v-bind="componentField"/>
                </FormControl>
                <FormMessage>no</FormMessage>
              </FormItem>
            </FormField>

            <FormField v-slot="{ componentField }" name="password">
              <FormItem v-auto-animate>
                <FormLabel>Password</FormLabel>
                <FormControl>
                  <Input type="password" placeholder="Your password in TSIMS" v-bind="componentField"/>
                </FormControl>
                <FormMessage/>
              </FormItem>
            </FormField>

            <Button type="submit">
              Submit
            </Button>
          </Form>
        </div>
          <Card class="shadow-none mt-6" v-auto-animate v-if="authDeletionSuccessful">
            <CardHeader>
              <CardTitle>Authentication Successful!</CardTitle>
              <CardDescription>You will no longer receive notifications.</CardDescription>
            </CardHeader>
          </Card>
      </TabsContent>
    </Tabs>
  </div>
  <Toaster />
</template>