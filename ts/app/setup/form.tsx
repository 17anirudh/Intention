"use client"

import { useForm } from "react-hook-form"
import { zodResolver } from "@hookform/resolvers/zod"
import { z } from "zod"
import { toast } from "sonner"
import { Form } from "@/components/ui/form"
import {
  Field,
  FieldLabel,
  FieldDescription,
  FieldError
} from "@/components/ui/field"
import {
  Button
} from "@/components/ui/button"
import {
  Input
} from "@/components/ui/input"
import {
  Textarea
} from "@/components/ui/textarea"
import { useState } from "react"

const formSchema = z.object({
  ngo_name: z.string().min(1).min(3).max(262),
  ngo_desc: z.string().min(10).max(1000),
  ngo_established: z.coerce.date(),
  ngo_contact: z.string(),
  ngo_email: z.string(),
  ngo_location: z.tuple([z.string().min(1), z.string().optional()]),
  ngo_emp_count: z.number().min(2)
});

export default function MyForm() {

  const [countryName, setCountryName] = useState<string>('')
  const [stateName, setStateName] = useState<string>('')

  const form = useForm<z.infer<typeof formSchema>>({
    resolver: zodResolver(formSchema),
    defaultValues: {
      "ngo_established": new Date()
    },
  })

  function onSubmit(values: z.infer<typeof formSchema>) {
    try {
      console.log(values);
      toast(
        <pre className="mt-2 w-[340px] rounded-md bg-slate-950 p-4">
          <code className="text-white">{JSON.stringify(values, null, 2)}</code>
        </pre>
      );
    } catch (error) {
      console.error("Form submission error", error);
      toast.error("Failed to submit the form. Please try again.");
    }
  }

  return (
    <Form {...form}>
      <form onSubmit={form.handleSubmit(onSubmit)} className="space-y-8 max-w-3xl mx-auto py-10">
        
        <div className="grid grid-cols-12 gap-4">
          
          <div className="col-span-4">
            <Field>
  <FieldLabel htmlFor="ngo_name">NGO name</FieldLabel>
  <Input 
    id="ngo_name" 
    placeholder=""
    
    {...form.register("ngo_name")}
  />
  <FieldDescription>This is the name of your NGO</FieldDescription>
  <FieldError>{form.formState.errors.ngo_name?.message}</FieldError>
</Field>
          </div>
          
        </div>
        <Field>
  <FieldLabel htmlFor="ngo_desc">Description</FieldLabel>
  <Textarea 
    id="ngo_desc" 
    placeholder=""
    
    {...form.register("ngo_desc")}
  />
  <FieldDescription>This is the description of what is your NGO and it's work</FieldDescription>
  <FieldError>{form.formState.errors.ngo_desc?.message}</FieldError>
</Field>
        <Field>
  <FieldLabel htmlFor="ngo_established">Date of establishment</FieldLabel>
  <Input 
    id="ngo_established" 
    placeholder=""
    {...form.register("ngo_established")}
  />
  <FieldDescription>Date of establishment of your NGO</FieldDescription>
  <FieldError>{form.formState.errors.ngo_established?.message}</FieldError>
</Field>
        
        <div className="grid grid-cols-12 gap-4">
          
          <div className="col-span-4">
            <Field>
  <FieldLabel htmlFor="ngo_contact">Phone number</FieldLabel>
  <Input 
    id="ngo_contact" 
    placeholder="Placeholder"
    {...form.register("ngo_contact")}
  />
  <FieldDescription>Enter your valid phone number.</FieldDescription>
  <FieldError>{form.formState.errors.ngo_contact?.message}</FieldError>
</Field>
          </div>
          
        </div>
        <Field>
  <FieldLabel htmlFor="ngo_email">Email</FieldLabel>
  <Input 
    id="ngo_email" 
    placeholder=""
    
    {...form.register("ngo_email")}
  />
  <FieldDescription>Enter your valid email id</FieldDescription>
  <FieldError>{form.formState.errors.ngo_email?.message}</FieldError>
</Field>
        
        <div className="grid grid-cols-12 gap-4">
          
          <div className="col-span-4">
            <Field>
  <FieldLabel htmlFor="ngo_location">Select Location</FieldLabel>
  <Input 
    id="ngo_location" 
    placeholder="Placeholder"
    {...form.register("ngo_location")}
  />
  <FieldDescription>Select Country and State/Province</FieldDescription>
  <FieldError>{form.formState.errors.ngo_location?.message}</FieldError>
</Field>
          </div>
          
        </div>
        <Field>
  <FieldLabel htmlFor="ngo_emp_count">No.of Volunteers</FieldLabel>
  <Input 
    id="ngo_emp_count" 
    placeholder="10"
    
    {...form.register("ngo_emp_count")}
  />
  <FieldDescription>Current no.of employees working</FieldDescription>
  <FieldError>{form.formState.errors.name_3513544575?.message}</FieldError>
</Field>
        <Button type="submit">Submit</Button>
      </form>
    </Form>
  )
}