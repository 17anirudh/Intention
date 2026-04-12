import Link from "next/link"
import { ROUTE } from "@/lib/routes"
import Image from "next/image"
import Silk from "@/components/ui/Silk"

export default function Home() {
  return (
    <div className="relative">
      <Silk 
        speed={2}
        scale={0.8}
        color="#1a2b2e"
        noiseIntensity={1.5}
        rotation={0}
      />
      <main className="w-screen min-h-screen absolute flex flex-col gap-3 justify-center items-center">
        <section id="hero" className="min-h-screen w-full flex flex-col gap-3 justify-center items-center">
          <div className="flex flex-col gap-2 items-center">
            <div role="img" className="w-20 h-20 relative">
              <Image src="/logo.webp" alt="Logo" fill sizes="80px" className="active:scale-75 hover:scale-105 transition-all duration-300 rounded-4xl" />
            </div>
            <h1 className="text-4xl font-heading">Intention</h1>
          </div>
          <h2 className="text-xl font-serif wrap-break-word text-pretty">
            We <span className="underline">parse</span> your data and identify <span className="underline">goals</span> and make you visible
          </h2>
          <Link 
            href={ROUTE.dashboard.home} 
            className="active:scale-75 hover:scale-105 transition-all duration-300 border p-2 rounded-4xl"
            title="Go to login"
            >
              Get Started
            </Link>
        </section>
      </main>
    </div>
  )
}