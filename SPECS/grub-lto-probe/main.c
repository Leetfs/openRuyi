/*
 * SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
 * SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
 * SPDX-License-Identifier: MulanPSL-2.0
 */

int invoke_target(void);
int __wrap_target(void);

int __wrap_target(void)
{
    return 0;
}

int main(void)
{
    return invoke_target();
}
