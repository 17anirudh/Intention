import type { ReactNode } from "react";

export default function DashboardLayout({ children }: { children: ReactNode }) {
    return (
    <div className="relative w-screen h-screen text-background">
        <div
            aria-hidden="true"
            className="pointer-events-none absolute inset-0"
            style={{
                backgroundImage: `url("/bg.png")`,
                backgroundRepeat: "repeat",
                opacity: 0.39,
            }}
        />
        <main className="flex flex-col gap-2 justify-center items-center w-full">
            {children}
        </main>
    </div>
    )
}