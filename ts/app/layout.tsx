import type { Metadata } from "next";
import { Geist, Geist_Mono, Manrope, Lora } from "next/font/google";
import "./globals.css";
import type { ReactNode } from "react";
import Silk from "@/components/ui/Silk";

const loraHeading = Lora({subsets:['latin'],variable:'--font-heading'});
const manrope = Manrope({subsets:['latin'],variable:'--font-sans'});
const geistSans = Geist({ variable: "--font-geist-sans", subsets: ["latin"] });
const geistMono = Geist_Mono({variable: "--font-geist-mono", subsets: ["latin"]});

export const metadata: Metadata = {
  title: "Uncapped",
  description: "Orchestrator for NGOs for Smart Resource Allocation",
  icons: {
    icon: '/logo.webp'
  }
};

type Props = { children: ReactNode }

export default function RootLayout({ children }: Readonly<Props>) {
  return (
    <html lang="en" className={`antialiased ${geistSans.variable} ${geistMono.variable} font-sans ${manrope.variable} ${loraHeading.variable}`}>
      <body className="h-screen w-screen bg-foreground text-background relative overflow-x-hidden">
        {children}
      </body>
    </html>
  );
}
