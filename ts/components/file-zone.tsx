"use client";

import { useState, useRef, ChangeEvent } from "react";
import { CloudUploadIcon, FileIcon, XIcon, FileSymlinkIcon } from "lucide-react";
import { useDropzone } from "react-dropzone";
import Image from "next/image";

export function FilesZone() {
    const fileInputRef = useRef<HTMLInputElement | null>(null);
    const [fileItem, setFileItem] = useState<File[]>([]);

    function handleFileChange(e: ChangeEvent<HTMLInputElement>) {
        if (e.target.files) {
            const newFiles = Array.from(e.target.files);
            setFileItem(prev => [...prev, ...newFiles]);
        }
    };

    const { getRootProps, getInputProps, isDragActive } = useDropzone({
        onDrop: acceptedFiles => {
            setFileItem(prev => [...prev, ...acceptedFiles]);
        }
    });

    async function handleUpload() {
        if (!fileItem || fileItem.length === 0) {
            return;
        }
    };

    function handlePreview(f: File) {
        window.open(URL.createObjectURL(f), '_blank')
    };

    return (
        <div className="w-full flex flex-col items-center justify-center" {...getRootProps()}>
            <div className="w-full min-h-[10vh] max-w-md border border-gray-200 rounded-lg">
                <input 
                    {...getInputProps()} 
                    type="file" 
                    hidden 
                    onChange={handleFileChange} 
                    multiple 
                    ref={fileInputRef}
                    accept="image/*, .pdf, .docx, .xlsx, .txt" 
                />
                <div className="flex flex-col gap-2 p-4">
                    <button
                        role="button"
                        onClick={() => { fileInputRef.current?.click() }}
                        className="w-full p-2 flex justify-center"
                    >
                        <CloudUploadIcon size={50}  className="active:scale-75 hover:scale-125 duration-150 transition-all cursor-pointer" />
                    </button>
                    {fileItem.map((item, index) => (
                        <div key={index} className="flex gap-2 items-center flex-wrap">
                            <FileIcon />
                            <span className="w-[50px] sm:w-[100px] truncate">{item.name}</span>
                            <span>{(item.size / 1024 / 1024).toFixed(2)} MB</span>
                            <button 
                                className="cursor-pointer"
                                onClick={() => setFileItem(prev => prev.filter((_, i) => i !== index))}
                            >
                                <XIcon color="red" />
                            </button>
                            <button 
                                className="cursor-pointer"
                                onClick={() => handlePreview(item) }
                            >
                                <FileSymlinkIcon />
                            </button>
                        </div>
                    ))}
                    {isDragActive ? 
                        <p>Drop the files here ...</p> : 
                        <p>Drag 'n' drop files here, or click to select files</p>
                    }
                    {fileItem.length > 0 && (
                        <button
                            role="submit"
                            onClick={handleUpload}
                        >
                            Upload
                        </button>
                    )}
                </div>
            </div>
        </div>
    )
}

type Props = {
    fileType: "image" | "any"
}

export function FileZone({ fileType }: Props) {
    const fileInputRef = useRef<HTMLInputElement | null>(null);
    const [fileItem, setFileItem] = useState<File | null>(null);

    function handleFileChange(e: ChangeEvent<HTMLInputElement>) {
        if (e.target.files) {
            const newFiles = Array.from(e.target.files);
            setFileItem(newFiles[0]);
        }
    };

    const { getRootProps, getInputProps, isDragActive } = useDropzone({
        onDrop: acceptedFiles => {
            setFileItem(acceptedFiles[0]);
        }
    });

    async function handleUpload() {
        if (!fileItem) {
            return;
        }
    };

    function imagePreview(f: File) {
        const url = URL.createObjectURL(f);
        return url;
    }

    function handlePreview(f: File) {
        window.open(URL.createObjectURL(f), '_blank')
    };

    return (
        <div className="w-full flex flex-col items-center justify-center" {...getRootProps()}>
            <div className="w-full min-h-[10vh] max-w-md border border-gray-200 rounded-lg">
                <input 
                    {...getInputProps()} 
                    type="file" 
                    hidden 
                    onChange={handleFileChange} 
                    ref={fileInputRef}
                    accept={fileType === "image" ? "image/*" : "*/*"} 
                />
                <div className="flex flex-col gap-2 p-4">
                    <button
                        role="button"
                        onClick={() => { fileInputRef.current?.click() }}
                        className="w-full p-2 flex justify-center"
                    >
                        <CloudUploadIcon size={50}  className="active:scale-75 hover:scale-125 duration-150 transition-all cursor-pointer" />
                    </button>
                    {fileItem && (
                        <div key={0} className="flex gap-2 items-center flex-wrap">
                            <FileIcon />
                            <span className="w-[50px] sm:w-[100px] truncate">{fileItem.name}</span>
                            <span>{(fileItem.size / 1024 / 1024).toFixed(2)} MB</span>
                            <button 
                                className="cursor-pointer"
                                onClick={() => setFileItem(null)}
                            >
                                <XIcon color="red" />
                            </button>
                            {fileType === "image" ? (
                                <Image 
                                    src={imagePreview(fileItem)} 
                                    alt="preview" 
                                    width={100} 
                                    height={100}
                                    onClick={() => handlePreview(fileItem)}
                                    className="active:scale-90 hover:scale-110 duration-300 transition-all" 
                                />
                            ) : (
                                <button 
                                    className="cursor-pointer"
                                    onClick={() => handlePreview(fileItem) }
                                >
                                    <FileSymlinkIcon />
                                </button>
                            )}
                        </div>
                    )}
                    {isDragActive ? 
                        <p>Drop the files here ...</p> : 
                        <p>Drag 'n' drop files here, or click to select files</p>
                    }
                    {fileItem && (
                        <button
                            role="submit"
                            onClick={handleUpload}
                        >
                            Upload
                        </button>
                    )}
                </div>
            </div>
        </div>
    )
}