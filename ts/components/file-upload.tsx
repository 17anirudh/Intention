'use client';

import { useState, useRef, ChangeEvent } from "react";
import { CloudUploadIcon, FileIcon, XIcon, FileSymlinkIcon } from "lucide-react";
import { useDropzone } from "react-dropzone";

export default function FileUpload() {
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
        <div className="w-full flex flex-col items-center justify-center">
            <div className="w-full min-h-[10vh] max-w-md border border-gray-200 rounded-lg" {...getRootProps()}>
                <input 
                    {...getInputProps()} 
                    type="file" 
                    hidden 
                    onChange={handleFileChange} 
                    multiple 
                    ref={fileInputRef} 
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