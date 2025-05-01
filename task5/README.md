# Task 5: Hashing & Integrity Check Utility

## Description

This task demonstrates how to use cryptographic hash functions (SHA-256, SHA-1, MD5) to check file integrity.

## Files

- `original.txt` – Original file content
- `tampered.txt` – Modified version of the file
- `hashes.json` – Hash values of the original file
- `integrity_check_result.txt` – Output showing whether tampered file still matches original hashes

## How It Works

1. Hashes of the original file are stored in `hashes.json`.
2. A separate tampered file is created.
3. The script recalculates hashes and compares with the originals.
4. If any hash differs, integrity check fails.

## Expected Result

SHA-256 Check: FAIL  
SHA-1 Check: FAIL  
MD5 Check: FAIL
